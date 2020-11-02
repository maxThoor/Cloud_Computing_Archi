# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 15:27:26 2020

@author: louis
"""

import requests
import json
from pymongo import MongoClient
from bson import ObjectId
import datetime


def get_vlille():
    url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=-1&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("records", [])

atlas = MongoClient('mongodb+srv://ludo:MdaPgzDrdE7T5D9C@projetmongo.sm79j.mongodb.net/<dbname>?retryWrites=true&w=majority')

db = atlas.bicycle

db.datas.create_index([('station_id', 1),('date', -1)], unique=True)

def station_to_find(name):
    
    station = db.stationvelo.find({"name" : {'$regex':"^" + name}})
    
    return (list(station))

#print(station_to_find("Rue"))


def station_to_delete(name):   
    db.stationvelo.delete_one({"name" : name})

#station_to_delete("Opera")
    

def station_to_update(ID ,updatedname):
    db.stationvelo.update_one({"_id" : ObjectId(ID)}, { "$set" :{ "name" : updatedname}})
    
#station_to_update("5fa0129da5fc2095b2ad9b84","test")

def deactivate_area(lat, lon, dist):
    trouve= db.stationvelo.find({"Geo": {"$near": {"$geometry":{"type": "Point","coordinates": [lat, lon]},"$maxDistance": dist}}, "Available":"True"})
    for i in trouve:
        db.stationvelo.update_one({"_id":i["_id"]}, {"$set": {"Available": "False"}},upsert = True)

