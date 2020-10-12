# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 12:00:57 2020

@author: maxou
"""

import requests
import json

def get_vlille():
    url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion"
    response_lille = requests.request("GET",url)
    response_json_lille = json.loads(response_lille.text.encode('utf8'))
    return response_json_lille.get("records",[])

def get_vlyon():
    url = "https://public.opendatasoft.com/api/records/1.0/search/?dataset=station-velov-grand-lyon&q=&rows=2000&facet=name&facet=commune&facet=bonus&facet=status&facet=available&facet=availabl_1&facet=availabili&facet=availabi_1&facet=last_upd_1"
    response_lyon = requests.request("GET",url)
    response_json_lyon = json.loads(response_lyon.text.encode('utf8'))
    return response_json_lyon.get("records",[])

def get_vparis():
    url = "https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes"
    response_paris = requests.request("GET",url)
    response_json_paris = json.loads(response_paris.text.encode('utf8'))
    return response_json_paris.get("records",[])

def get_vrennes():
    url = "https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=etat-des-stations-le-velo-star-en-temps-reel&q=&facet=nom&facet=etat&facet=nombreemplacementsactuels&facet=nombreemplacementsdisponibles&facet=nombrevelosdisponibles"
    response_rennes = requests.request("GET",url)
    response_json_rennes = json.loads(response_rennes.text.encode('utf8'))
    return response_json_rennes.get("records",[])


