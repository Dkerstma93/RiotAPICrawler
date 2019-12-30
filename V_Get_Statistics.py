from V_Get_Summoners import match_id_list
from V_Get_Summoners import api
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Password123",
  database="vilemawdb"

)
mycursor = mydb.cursor()

def get_match_stats():
  index = 0
  match_stats = api.get_matchstats(match_id_list[0])
  while index < 10:
    print(match_stats['participants'][index]['stats']['item0'])
    print(match_stats['participants'][index]['championId'])
    index+=1



