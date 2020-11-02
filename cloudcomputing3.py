# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:32:52 2020

@author: louis
"""

from pymongo import MongoClient


client = MongoClient('mongodb+srv://ludo:MdaPgzDrdE7T5D9C@projetmongo.sm79j.mongodb.net/<dbname>?retryWrites=true&w=majority')

db = client.bicycle 
db.datas.create_index([('station_id', 1),('date', -1)], unique=True)

db.stationvelo.create_index([('geometry','2dsphere')])

def get_station_id(id_ext):
    tps = db.stationvelo.find_one({ 'source.id_ext': id_ext }, { '_id': 1 })
    return tps['_id']


def nearStation(lat,lon):
    
    near_station = db.stationvelo.find({'geometry':{
        '$near':{'$geometry':{
            'type': "Point",
            'coordinates': [lon,lat]},
            '$maxDistance':1000,
            '$minDistance':0
            }
        }})
    return(list(near_station))
    

print(nearStation(50.66026,3.087567))


    

