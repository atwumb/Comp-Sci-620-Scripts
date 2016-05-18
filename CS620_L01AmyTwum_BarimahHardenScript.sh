#!/bin/bash
#Author: Amy Twum-Barimah
#IAE 500 L01

#Check if the user is root.Only users who have rights to configure should have access to run these commands. Should be the root user.  
userid=`id | cut -d ' ' -f 1` #stores the userid for the current user 
if  [ "${userid}" != "uid=0(root)" ] 
then
  echo "You do not have permissions to run this script as a non-root user. Exiting..Have a nice day"
  exit # Exits script if user is not root. 
fi



echo "Checking the current system's date and time"
#Verifying the time is important to make sure system runs as scheduled.  Updates may be scheduled to run at a certain time.
date #displays the systems current date. 
tzone=`date +%Z` #hold the timezone abbrieviation in the date
if [ "${tzone}"   == "EST" ]
 then  
    echo "Time is in the current timezone"
 else 
    echo "Time is the wrong timezone"
fi
sleep 2 


#print 2 blank lines to separate the command outputs 
echo " "
echo " "
#Check the space in the root directory  is not taking up too space which affects system functionality. If it is near 100%, updates can not be installed

used_space=`df -k | tail -n +2 | head -1| awk '{print $5}' | sed 's/%//g'`
hname=`hostname`
if [ $used_space -gt 90 ]
then
 echo "Space used on /opt on box $used_space% and exceeded the amount of 90%, Please check the space"
else 
echo "Space used under root(/) directory on box is $used_space %"
fi
sleep 2

echo " "
echo " "

#Below gets the count of users configured for each shell
#Read each line in file, check the 7th field for user's shell value and get a count for the total users configured for each shell
echo "=============================="
echo "Number users configured for each shell:"
echo " "
for i in `cat /etc/passwd | cut -d: -f7 | sort -u` 
   do echo $i
   grep $i /etc/passwd| wc -l
done

user_logged=`cat /etc/passwd | cut -d: -f7 | sort -u|wc -l`

echo "The total number of users currently logged in is $user_logged" 

sleep 3 # pause the script for 3 seconds



#Check to see if users logged in are in the /etc/passwd with configures user accounts on local system
for i in  `who | cut -d ' ' -f 1`
do
num=`grep $i /etc/passwd | wc -l`
   if(( num >   0))
   then
    infile=$((infile+1)) #counter for number of  local user accounts
  else
    outfile=$((outfile+1))#counter for number of user accounts not managed locally
 fi
done


if((outfile > 0))
then
echo "Check the notmanaged.log for any user accounts not managed locally."
else
echo "All user accounts currently logged into the system are managed locally"
fi

sleep 3

echo " "
echo " "


sleep 3 
apt-get update && apt-get upgrade #Checking for updates to current package and installing updates

echo " "
sleep 3 
echo "#########Removing packages no longer needed"
sleep 3 
 
apt-get autoremove #Removes any package whose dependent package has been removed or no longer needed on it.
 
echo ""
echo ""
echo ""
echo ""
sleep 3


#check to see if /etc/password, owned by root
echo " "

echo "==============================="
echo "Checking /etc/passwd file to verify permissions and owner" 
#"/etc/paswd file list all the system local accounts. Only root user should have write perimissions and own the file 
ls -l /etc/passwd | 
awk '
$3 == "root" && $1 != "-rw-r--r--"{
print "Owner of '$3' is root, wrong permissions, should be -rw-r--r--.  Action needed"}
$3 == "root" && $1 == "-rw-r--r--"{
 print "Owner of  is root, right permissions. No action needed"}
$3 != "root" && $1 == "-rw-r--r--"{
 print "Owner is not root, right permission. Action needed. "}
$3 != "root" && $1 != "-rw-r--r--"{
 print "Owner is not root, wrong permissions, should be -rw-r--r--. Action needed"
}'



echo " "
echo " "

#check firewall status , activate v if it is inactive  
echo "#######################################"
echo "Checking whether firewall is enabled"
echo " "

if ufw status  | grep -q  inactive | cut -d ' ' -f2
then 
  ufw enable # enable firewall
fi



