# -*- coding: utf-8 -*-
from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, , requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse,subprocess,unicodedata,GACSender
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()
#==============================================================================#
line = LINE()
#line = LINE("เมล","พาส")
#line = LINE('')
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))

print ("Login Succes")

lineMID = line.profile u7a95e1c0ad51d08814e319acbc3fbba7.mid
lineProfile = line.getProfile(u7a95e1c0ad51d08814e319acbc3fbba7)
lineSettings = line.getSettings(u7a95e1c0ad51d08814e319acbc3fbba7)
