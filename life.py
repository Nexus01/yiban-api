import os
import sys
import re
import json
import time
import getopt
import random
import requests

def wake():
    interval = random.uniform(500, 1000)
    print('the program will pause for',interval,'seconds')
    return time.sleep(interval)

def breakfast():
    interval = random.uniform(100, 150)
    print('the program will pause for',interval,'seconds')
    return time.sleep(interval)

def onclass():
    interval = 2700
    print('the program will pause for',interval,'seconds')
    return time.sleep(interval)

def rest():
    interval = 300
    print('the program will pause for',interval,'seconds')
    return time.sleep(interval)

def lunch():
    interval = random.uniform(900, 1500)
    print('the program will pause for',interval,'seconds')
    return time.sleep(interval)

def toilet():
    interval = random.uniform(180, 300)
    print('the program will pause for',interval,'seconds')
    return time.sleep(interval)

def dinner():
    interval = random.uniform(1500, 1700)
    print('the program will pause for',interval,'seconds')
    return time.sleep(interval)

def bed():
    interval = 3000
    print('the program will pause for',interval,'seconds')
    return time.sleep(interval)