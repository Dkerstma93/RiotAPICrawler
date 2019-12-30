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
summoner_list = []
rank_list = []
division_list = ['IV','III','II', 'I']
tier_list = ['IRON','BRONZE', 'SILVER', 'GOLD', 'PLATINUM', 'DIAMOND']

def save_summoners():
    index = 0
    for j in tier_list:
        for i in division_list:
            request_summoners = api.get_summoners('RANKED_SOLO_5x5',j,i)
            for x in request_summoners:
                summoner_list.append(x['summonerName'])
                rank_list.append(j + ' ' + i)

