import sys
import time
import random 
import datetime
import telepot

import RPi.GPIO as GPIO
import time
import smtplib
import tweepy
import pyowm

GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)

smtpUser='THEEMAIL@gmail.com'	
smtpPass=''

toAdd=['emailXXXX@gmail.com','email2XXXX@gmail.com','email3XXXX@gmail.com']
fromAdd=smtpUser


SUBJECT = 'ALERT ! Bridge BROKEN ! '
TEXT = 'ALERT ! Bridge no. 493, between Kandaghat and Kanoh[30.8 deg. N 70.1 deg. E] broke just now. Check the time of email to know when was it broken.this email has been autosent by a python script.'
SUBJECT1 = 'FIRE ALERT ! '
TEXT1 = 'FIRE ALERT ! Fire at Vivanta Mall, Solan[30.9045 deg. N, 77.0967 deg. E] .Check the time of this email to see when did it started.this email has been autosent by a python script. '
                  

#header = 'From : ' + fromAdd + 'Subject : ' + subject 
header1 = 'Subject :{}\n\n{}'.format(SUBJECT, TEXT)
header2 = 'Subject :{}\n\n{}'.format(SUBJECT1, TEXT1)

body = 'ALERT !!Bridge no. 493, between Kandaghat and Kanoh[30.8 deg. N 70.1 deg. E] broke just now!. Check the time of email to know when was it broken.this email has been autosent by a python script'

#########################################
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main1():
  
  cfg = { 
    "consumer_key"        : "YOURS PLEASE",
    "consumer_secret"     : "YOURS PLEASE",
    "access_token"        : "YOURS PLEASE",
    "access_token_secret" : "YOURS PLEASE" 
    }

  api = get_api(cfg)
  tweet = "$$.ALERT! Bridge no..493, which is between Kandaghat and Kanoh broke just now!."
  
  
  status = api.update_status(status=tweet) 

#_______________________________________#


def main2():
  
  cfg = { 
    "consumer_key"        : "YOURS PLEASE",
    "consumer_secret"     : "YOURS PLEASE",
    "access_token"        : "YOURS PLEASE",
    "access_token_secret" : "YOURS PLEASE" 
    }

  api = get_api(cfg)
  tweet = " $$.FIRE ALERT ! Fire at Vivanta Mall, Solan[30.9045 deg.. N, 77.0967 deg. E] "
  
  
  status = api.update_status(status=tweet) 


#_______________________________________#  

 #########################################

 ##-------------------------------------##

#def sendImage():
 #   url = "https://api.telegram.org/bot<Token>/sendPhoto";
  #  files = {'photo': open('img.jpg', 'rb')}
   # data = {'chat_id' : "-177094990'"}
   # r= requests.post(url, files=files, data=data)
    #print(r.status_code, r.reason, r.content)


 ##-------------------------------------## 
s=smtplib.SMTP('smtp.gmail.com',587)
s.ehlo()
s.starttls()
s.ehlo()
s.login(smtpUser,smtpPass)


####+++++++++++++++++++++++++++############

owm = pyowm.OWM('6742f3b7da92a96a971d6c39b284806e')  


#forecast = owm.daily_forecast("Milan,it")
#tomorrow = pyowm.timeutils.tomorrow()
#forecast.will_be_sunny_at(tomorrow)  

# Search for current weather in London (UK)
observation = owm.weather_at_place('Solan,in')
w = observation.get_weather()
#print(w)                      
                              

# Weather details
wind = w.get_wind()                  
humidity = w.get_humidity()              
temp = w.get_temperature('celsius')  

observation_list = owm.weather_around_coords(-22.57, -43.12)

####++++++++++++++++++++++++++++############
while 1 :

     input_state = GPIO.input(18)
     input_state1 = GPIO.input(23)
     
     if input_state == True and input_state1 == False : 
           print("Bridge is broken ! Sending alert messages on all channels .")
           
           #s.sendmail(fromAdd, toAdd, header + '\n' + body)
           s.sendmail(fromAdd, toAdd, header1)
           
           chat_id1 = '-177094990'
           file_id1 = 'http://mw2.google.com/mw-panoramio/photos/medium/88068769.jpg' 
           bot=telepot.Bot('319826203:AAFtepbgGeh01st22GIFQAHk_gC8ZE8qpvE')                                                          
           bot.sendMessage(chat_id1,' Bridge no.493, between Kandaghat and Kanoh[30.8 deg. N, 77.8 deg. E] IS BROKEN !! ')
           bot.sendPhoto(chat_id1,file_id1)
           bot.sendMessage(chat_id1,'Here are some physical conditions : - ')
           bot.sendMessage(chat_id1,'Wind speed and direction(in degree) : ')           
           bot.sendMessage(chat_id1,wind)
           bot.sendMessage(chat_id1,'The humidity percentage is : ')           
           bot.sendMessage(chat_id1,humidity)
           bot.sendMessage(chat_id1,'Temperature conditions : ')                      
           bot.sendMessage(chat_id1,temp)
           
           main1()
                 #print(chat_id) 
           #sendImage()  
           print("FIRE ALERT ! Sending alert messages on all channels .")
           #s.sendmail(fromAdd, toAdd, header + '\n' + body)
           s.sendmail(fromAdd, toAdd, header2)
           
           chat_id2 = '-182305252'
           file_id2 = 'http://p4.img.cctvpic.com/20110410/images/1302401900517_1302401900517_r.jpg' 
           bot=telepot.Bot('359180213:AAEcu9w8jqMbUDiInEtSdfJczW7j6vjTHjY')                                                          
           bot.sendMessage(chat_id2,' FIRE ALERT !.. Fire at Vivanta Mall, Solan[30.9045 deg. N, 77.0967 deg. E]')
           bot.sendPhoto(chat_id2,file_id2)                                              
           bot.sendMessage(chat_id2,'Here are some physical conditions : - ')
           bot.sendMessage(chat_id2,'Wind speed and direction(in degree) : ')                      
           bot.sendMessage(chat_id2,wind)
           bot.sendMessage(chat_id2,'The humidity percentage is : ')           
           
           bot.sendMessage(chat_id2,humidity)
           bot.sendMessage(chat_id2,'Temperature conditions : ')
           bot.sendMessage(chat_id2,temp)
           main2()                                             
                                                         
           #bot.message_loop(handle)
           #def handle(msg) :
           #    chat_id = msg['chat']['id']
           #    chat_id1 = '-177094990'
           #    command = msg['text']
              
            #   if command == '/alivebridge' :
            #     bot.sendMessage(chat_id, 'Bridge no.493^, between Kandaghat and Kanoh[30.8 deg. N, 77.8 deg. E] IS BROKEN !! ')
                 #print(chat_id) 
                 #sendImage()
            #   elif command == '/time' :                                      
            #     bot.sendMessage(chat_id, str(datetime.datetime.now()))
            #   if command == '/alivefire' :
            #     bot.sendMessage(chat_id, 'XFIRE ALERT ! Fire at Vivanta Mall, Solan[30.9045 deg. N, 77.0967 deg. E] .')
                                                        
          # bot=telepot.Bot('319826203:AAFtepbgGeh01st22GIFQAHk_gC8ZE8qpvE')                                               
          # bot.message_loop(handle) 
           
           #while 1:
           #time.sleep(5)
           #import summed3  
     #----------------------both conditions being true ends
        
     elif input_state == True : 
           print("Bridge is broken ! Sending alert messages on all channels .")
           #s.sendmail(fromAdd, toAdd, header + '\n' + body)
           s.sendmail(fromAdd, toAdd, header1)
           main1()
           chat_id1 = '-177094990'
           file_id1 = 'http://mw2.google.com/mw-panoramio/photos/medium/88068769.jpg' 
           bot=telepot.Bot('319826203:AAFtepbgGeh01st22GIFQAHk_gC8ZE8qpvE')                                                          
           bot.sendMessage(chat_id1,' Bridge no.493, between Kandaghat and Kanoh[30.8 deg. N, 77.8 deg. E] IS BROKEN !! ')
           bot.sendPhoto(chat_id1,file_id1)  
           bot.sendMessage(chat_id1,'Here are some physical conditions : - ')
           bot.sendMessage(chat_id1,'Wind speed and direction(in degree) : ')                     
           bot.sendMessage(chat_id1,wind)
           bot.sendMessage(chat_id1,'The humidity percentage is : ')                      
           bot.sendMessage(chat_id1,humidity)
           bot.sendMessage(chat_id1,'Temperature conditions : ')
           bot.sendMessage(chat_id1,temp)
                 #print(chat_id) 
           #sendImage()  
                                                        
           #bot.message_loop(handle)
           #def handle(msg) :
           #    chat_id = msg['chat']['id']
           #    chat_id1 = '-177094990'
           #    command = msg['text']
              
           #    if command == '/alive' :
           #      bot.sendMessage(chat_id, 'Bridge no.493, between Kandaghat and Kanoh[30.8 deg. N, 77.8 deg. E] IS BROKEN !! ')
                 #print(chat_id) 
                 #sendImage()
           #    elif command == '/time' :                                      
            #     bot.sendMessage(chat_id, str(datetime.datetime.now()))
                                                        
         #  bot=telepot.Bot('319826203:AAFtepbgGeh01st22GIFQAHk_gC8ZE8qpvE')                                               
         #  bot.message_loop(handle) 
           
         #  while 1:
         #   time.sleep(5)
           #import summed3
     elif input_state1 == False :
           print("FIRE ALERT ! Sending alert messages on all channels .")
           #s.sendmail(fromAdd, toAdd, header + '\n' + body)
           s.sendmail(fromAdd, toAdd, header2)
           main2()
           chat_id2 = '-182305252'
           file_id2 = 'http://p4.img.cctvpic.com/20110410/images/1302401900517_1302401900517_r.jpg' 
           bot=telepot.Bot('359180213:AAEcu9w8jqMbUDiInEtSdfJczW7j6vjTHjY')                                                          
           bot.sendMessage(chat_id2,' FIRE ALERT ! Fire at Vivanta Mall, Solan[30.9045 deg. N, 77.0967 deg. E]')
           bot.sendPhoto(chat_id2,file_id2)  
           bot.sendMessage(chat_id2,'Here are some physical conditions : - ')
           bot.sendMessage(chat_id2,'Wind speed and direction(in degree) : ')                      
           bot.sendMessage(chat_id2,wind)
           bot.sendMessage(chat_id2,'The humidity percentage is : ')                      
           bot.sendMessage(chat_id2,humidity)
           bot.sendMessage(chat_id2,'Temperature conditions : ')
           bot.sendMessage(chat_id2,temp)
                 #print(chat_id) 
           #sendImage()  
                                                        
           #bot.message_loop(handle)
          # def handle(msg) :
          #     chat_id = msg['chat']['id']
          #     chat_id2 = '-182305252'
          #     command = msg['text']
              
          #     if command == '/alive' :
          #       bot.sendMessage(chat_id, 'FIRE ALERT ! Fire at Vivanta Mall, Solan[30.9045 deg. N, 77.0967 deg. E] . ')
                 #print(chat_id) 
                 #sendImage()
          #     elif command == '/time' :                                      
          #       bot.sendMessage(chat_id, str(datetime.datetime.now()))
                                                        
         #  bot=telepot.Bot('359180213:AAEcu9w8jqMbUDiInEtSdfJczW7j6vjTHjY')                                               
         #  bot.message_loop(handle) 
           
         #  while 1:
         #   time.sleep(5)
           #import summed3
     else :
           print('The bridge is safe and no signs of any fire in any place')
           exit()
