import sqlite3
import requests
from random import randint
import GETAPI
import GetDB
from Coctel import Coctel

class APICOCTEL(GETAPI.GETAPI):
    def searchName(self, bebida_name):
        url= 'http://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + bebida_name
        response = requests.get(url)
        
        if response.status_code == 200:
            response_json = response.json()
            idbebida = response_json['coctels']
            
        
        