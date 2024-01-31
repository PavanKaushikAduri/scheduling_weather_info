#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------------
# Created By  : Pavan Kaushik Aduri
# Created Date: 30/01/2024
# version ='1.0'
# Description : This code builds required objects to fetch todays weather details\
#               and send it to users email.
# ----------------------------------------------------------------------------------

import sys
from getWeatherDataBuilder import GetWeatherDataBuilder
from sendWeatherInfoEmail import SendWeatherInfoEmail

if __name__ == "__main__":
    print("=" * 50)
    print("\n{0}Weather Info CLI Tool\n".format(" "*15))
    print("="*50)
    zip_code = input("\nPlease enter zip code : ")
    location = input("\nPlease enter location : ")
    metric = input("\nPlease enter units [Fahrenheit use units=imperial, Celsius use units=metric] : ")
    rec_email = input("\nPlease enter your email to send weather updates : ")
    
    print("\nMake sure you have your API KEY in apikey.txt file")
    print("\nChecking if API KEY exists...")

    try:
        with open('apikey.txt', 'r')as p:
            api_key = p.read()
    except Exception as e:
        print("\nAPI KEY not found in apikey.txt file!")
        sys.exit(1)
    
    print('\nAPI KEY Found! Fetching Weather Data...\n')
    
    weather_deatils_object = GetWeatherDataBuilder\
                                .getObject()\
                                .setZipCode(zip_code)\
                                .setLocation(location)\
                                .setApiKey(api_key)\
                                .setUnit(metric)\
                                .build()
    
    weather_deatils_object.fetchWeatherDeatils()
    SendWeatherInfoEmail(rec_email).sendEmail()