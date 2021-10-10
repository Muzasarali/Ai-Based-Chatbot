import pymongo
import json
import requests
from pymongo import MongoClient
import requests as rs
import math
class MyMongoDB:
    client = pymongo.MongoClient('localhost:27017')
    MYDB = client['TravelBot']
    PLACES = MYDB.places
    HOTEL = MYDB.hotels


    def insert(collection, data):
        temp = collection.insert_one(data)
        print(temp)
        return(temp)

    def find_document(collection, elements, multiple=True):
        if multiple:
            results = collection.find(elements)
            return results
        else:
            return collection.find_one(elements)
        
    def find_document_limit(collection, elements, limit, multiple=True):
        if multiple:
            results = collection.find(elements).limit(limit)
            return [r for r in results]
        else:
            return collection.find_one(elements)

    def find_random(cols, size,multiple=True):
        # results = self.PLACES.aggregate([{"$sample":{"size":5}}]);
        results = cols.aggregate([{"$sample":{"size":size}}]);
        for r in results:
            return [r for r in results]
    
    def findbus(src,dst,date):
        
        data = {
            'alibag': 77336,
            'panchgani': 446,
            'lonavala': 722,
            'mahabaleshwar': 445,
            'pune': 130
        }

        h2 = {
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5"
        }
        s = data[src]
        d = data[dst]
        baseURL = f'https://www.redbus.in/search/SearchResults?fromCity={s}&toCity={d}&DOJ=25-Jun-2021&sectionId=0&groupId=0&limit=0&offset=0&sort=0&sortOrder=0&meta=true&returnSearch=0'
        response = rs.post(baseURL, headers= h2)
        x = response.json()
        try: 
            if 'inv' in x:
                c = 0
                for i in range(5):
                    m = x['inv'][c]
                    print("",m['Tvs'])
                    print("Bus Type: ", m['bt'])
                    print("Bus Fair: ₹", m['minfr'])
                    print("Travel Duration : ", math.floor((m['dur']/60)*100)/100,"hrs")
                    print("", (m['sn']))
                    c+=1
                return x
        except:
            return None
        else: 
            x = {"inv":"None"}
            return None
            

