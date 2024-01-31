#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------------
# Created By  : Pavan Kaushik Aduri
# Created Date: 30/01/2024
# version ='1.0'
# Description : Sends email to the user, post fetching the weather details.
# ----------------------------------------------------------------------------------

import json
import smtplib, ssl
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from filterWeatherData import FilterWeatherData
from userinfo import SENDER_EMAIL, SMTP_SERVER, PORT

class EmailNotSent(Exception):
    pass


class SendWeatherInfoEmail:
    
    """ 
    Sends the formatted weather details
        to the users gmail.

    Raises:
        EmailNotSent: When User gmail APP CREDENTIALS
                    is not authorized.
    """

    senders_email = SENDER_EMAIL
    smtp_server = SMTP_SERVER
    port = PORT
    
    def __init__(self, rec_email):
        
        """
        Initializing variables

        Args:
            rec_email (str): receivers email
        """
        self.rec_email = rec_email
        self.weather_data = FilterWeatherData.getFilterObject()\
                                .getWeatherDataFromFile()\
                                .filterWeatherData()
        self.weather_desc = self.weather_data.getWeatherDescription
        self.weather_temp = self.weather_data.getTemperatureInfo
        self.body = "\nDescription : {0}\nTemp Info : {1}".format(
            self.weather_desc,
            json.dumps(self.weather_temp, indent=4)
            )

    def sendEmail(self):
        
        """
        This method sends email to the users

        Raises:
            EmailNotSent: if user is not authorized
                        using gmail APP CREDENTIALS
                        email is not sent to user.
        """
        print("\nCreating SSL default Context...")
        context = ssl.create_default_context()
        try:
            msg = MIMEMultipart("alternative")
            msg["Subject"] = 'Weather Update Information'
            msg["From"] = SendWeatherInfoEmail.senders_email
            msg["To"] = self.rec_email
            msg.attach(MIMEText('\n{0}'.format(self.body)))
            server = smtplib.SMTP(SendWeatherInfoEmail.smtp_server,
                                  SendWeatherInfoEmail.port)
            server.starttls(context=context)
            email_password = input("\nEnter your gmail password to send email : ")
            server.login(SendWeatherInfoEmail.senders_email, email_password)
            server.sendmail(SendWeatherInfoEmail.senders_email,
                            self.rec_email,
                            msg.as_string())
            print("Email Sent Successfully!")
        except Exception as e:
            raise EmailNotSent(e)
        finally:
            server.quit()

        

