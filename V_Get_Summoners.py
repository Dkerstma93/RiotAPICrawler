from V_API import V_API
import mysql.connector
import time

api = V_API('RGAPI-e5beecbd-0e85-49b2-a722-e565c6402188') #Insert API key

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Password123",
  database="vilemawdb"

)
mycursor = mydb.cursor()
division_list = ['IV','III','II', 'I']
tier_list = ['IRON','BRONZE', 'SILVER', 'GOLD', 'PLATINUM', 'DIAMOND']

def save_summoners():
    for j in tier_list:
        for i in division_list:
            request_summoners = api.get_summoners('RANKED_SOLO_5x5',j,i)
            for x in request_summoners:
                #summoner_by_name = api.get_summoner_by_name(x['summonerName'])
                sql = "INSERT INTO summoners (summonername, summonerrank) VALUES (%s, %s)"
                val = (x['summonerName'], j + ' ' + i)
                mycursor.execute(sql, val)
                time.sleep(1.5)
    mydb.commit()
