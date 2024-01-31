#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------------
# Created By  : Pavan Kaushik Aduri
# Created Date: 30/01/2024
# version ='1.0'
# Description : Fetches Weather Details using openweathermap API
# ----------------------------------------------------------------------------------

import json
import requests
from apis import DEFAULT_API

class weatherDataNotFoundException(Exception):
    pass

class GetWeatherDetails(weatherDataNotFoundException):

    """
    Fetches the weather details using
    openweathermap API.

    Raises:
        weatherDataNotFoundException: if weather data is
        not retrieved.
    """

    default_api = DEFAULT_API

    def __init__(self, zip_code, location, api_key, unit):
        
        """
        Initializing variables

        Args:
            zip_code (str): any valid zipcode
            location (str): country code [ex: us, in]
            api_key (str): openweathermap API key
            unit (str): [Fahrenheit use units=imperial,
                    Celsius use units=metric]
        """
        self.zip_code = zip_code
        self.location = location
        self.api_key = api_key
        self.unit = unit
    
    def fetchWeatherDeatils(self):
        
        """
        Fetches weather data using openweathermap API
        and writes it to weatherinfp.json file

        Raises:
            weatherDataNotFoundException: if API is unable to
                            retrieve weather details
        """
        weather_req_url = GetWeatherDetails.default_api \
            + f'zip={self.zip_code},{self.location}&appid={self.api_key}&units={self.unit}'
        res = requests.get(url=weather_req_url)
        try:
            if res.status_code == 200:
                res_json = res.json()
                print(json.dumps(res_json,indent=4))
                with open('weatherinfo.json', 'w')as p:
                    p.write(json.dumps(res_json, indent=4))
        except Exception as e:
            print("\nUnable to fetch weather data")
            raise weatherDataNotFoundException(e)




