__author__ = 'atwumb'

#Name: Amy Twum-Barimah
# Course: CS-620 L01
#Assignment: Lab 3 Problem 2

import requests

def convert_to_cedis():
    """
    Converts currency from dollars(USD) to cedis (GHS) using the rate obtained from the moneyconverter.com site
    """

    #Assumption - This program assumes that user will input a valid number, no special characters, strings, etc

    us_curr = 'USD' #currency unit for US dollars
    gh_curr = 'GHS' #currency unit for Ghana dolloars
    print("This program currency from dollars into cedis.")
    print()
    answer = float(input("Enter the dollar amount to be converted(i.e 12.00): "))

    dollars = float(answer)

    #Get the current rate from moneyconverter.com by passing the current currency/what the currency needs to converted
    converter_url = ('http://themoneyconverter.com/%s/%s.aspx') %(us_curr, gh_curr) # pass the USD currency,  GHS currency to the converter website


    split1 = ('>%s/%s =') % (gh_curr, us_curr)  #on the site, the rate is list as to Currency/From Currency
    strip1 = '</textarea>' #The string is located in textarea tag.

    req_alt = requests.get(converter_url) #make request to website defined in urlalt
    #the rate is located in the html tags <textarea> next to the
    conversion_rate = float(req_alt.text.split(split1)[1].split(strip1)[0].strip()) ## extract the rate from the text  on the page
    print("Current Rate (Cedis/Dollars): %.2f " %conversion_rate)
    print("$%.2f dollar(s) converts to %.2f cedis" %(dollars, (dollars * conversion_rate)))


if __name__ == '__main__':
    convert_to_cedis()  # call the function
