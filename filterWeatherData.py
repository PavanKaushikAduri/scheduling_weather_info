#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------------
# Created By  : Pavan Kaushik Aduri
# Created Date: 30/01/2024
# version ='1.0'
# Description : Filters the weather data that is fetched using openweathermap API
# ----------------------------------------------------------------------------------

import json

class FilterWeatherData:

    """
    Filters "description" and
    "temperature" details from
    weather data fetched using
    openweathermap API
    """
    
    def __init__(self):
        
        """
        Initializing variables
        """
        self.weather_info = ""
        self.weather_desc = ""
        self.temp_info = ""

    @property
    def getWeatherInfo(self):
        
        """
        This is a property
        to get weather info

        Returns:
            str : weather data
                fetched from OWM API
        """
        return self.weather_info
    
    @property
    def getWeatherDescription(self):
        
        """
        This is a property
        to get the description field from
        weather data

        Returns:
            str: description field of
                weather data
        """
        return self.weather_desc
    
    @property
    def getTemperatureInfo(self):

        """
        This is a property
        to get the temperature field from
        weather data

        Returns:
            str: temperature field of
                weather data
        """
        return self.temp_info
    
    @staticmethod
    def getFilterObject():

        """
        This is a static method
        to ge this class object

        Returns:
            object: this class object
        """
        return FilterWeatherData()

    def getWeatherDataFromFile(self):
        
        """
        This method reads the weather data
        from the weatherinfo.json file

        Returns:
            object: this class object
        """
        with open('weatherinfo.json', 'r')as p:
            weather_info = p.read()
        self.weather_info = weather_info
        return self
    
    def filterWeatherData(self):

        """
        This method filters the weather data
        from the weatherinfo.json file
        specifically description and temperature
        details

        Returns:
            object: this class object
        """
        weather_data = json.loads(self.weather_info)
        self.weather_desc = weather_data['weather'][0]['description']
        self.temp_info = weather_data['main']
        return self
    
    



    
