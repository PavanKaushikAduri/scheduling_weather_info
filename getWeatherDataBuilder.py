#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------------
# Created By  : Pavan Kaushik Aduri
# Created Date: 30/01/2024
# version ='1.0'
# Description : Implemented Builder design pattern which is a creational design
#               pattern to build objects to fetch weather details.
# ----------------------------------------------------------------------------------

from getWeatherDetails import GetWeatherDetails

class GetWeatherDataBuilder:

    """
    This is a builder class to 
    build getWeatherDetails object.
    """
    def __init__(self):
        
        """
        Initializing varibles
        """
        self.zip_code = ""
        self.location = ""
        self.api_key = ""
        self.unit = ""
    
    @staticmethod
    def getObject():
        """
        This method is a static method
        and is called to build this class
        object.

        Returns:
            object : of this class
        """
        return GetWeatherDataBuilder()
    
    def setZipCode(self, zip_code):
        
        """
        This method sets the zip code

        Args:
            zip_code (str): any valid zipcode

        Returns:
            object : of this class
        """
        self.zip_code = zip_code
        return self

    def setLocation(self, location):
        
        """This method sets the location

        Args:
            location (str): any valid location

        Returns:
            object : of this class
        """
        self.location = location
        return self
    
    def setApiKey(self, api_key):
        
        """
        This methods sets the API key
        of openweathermap

        Args:
            api_key (str): openweathermap API Key

        Returns:
            object: of this class
        """
        self.api_key = api_key
        return self

    def setUnit(self, unit):
        
        """
        This method sets the unit
        celsius or fahrenheit
        or kelvin

        Args:
            metric (str): celsius or fahrenheit or kelvin


        Returns:
            object: of this class
        """
        self.unit = unit
        return self
    
    def build(self):
        
        """
        Builder method to build
        GetWeatherDetails Object

        Returns:
            object: of GetWeatherDetails
                class
        """
        return GetWeatherDetails(
            self.zip_code,
            self.location,
            self.api_key,
            self.unit
            )