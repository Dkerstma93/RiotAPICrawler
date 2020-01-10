from V_API import V_API
import time
from V_Database import mydb

api = V_API('RGAPI-12cdd90e-0577-48df-94a2-b09d8b2f4310')  # Insert API key

cursor = mydb.cursor()

summoner_list = []
summoner_division_list = []
summoner_id_list = []
match_id_list = []

# fills summoner_list[] with summonersnames from each division and tier
def save_summoners(division, tier):
    request_summoners = api.get_summoners('RANKED_SOLO_5x5',division,tier)
    time.sleep(1)
    for x in request_summoners:
        summoner_list.append(x['summonerName'])
    index = 0
    for x in summoner_list:
        try:
            request_summonerid = api.get_summoner_by_name(x)
            time.sleep(1)
            summoner_id_list.append(request_summonerid['accountId'])
            index+=1
        except:
            index+=1
            continue
    save_match_id()

# #Use account ids to request matchids
def save_match_id():
    for x in summoner_id_list:
        request_matchids = api.get_match_history(x)
        time.sleep(1)
        index = 0
        try:
            for y in request_matchids['matches']:
                match_id_list.append(request_matchids['matches'][index]['gameId'])
                index +=1
        except:
            index +=1
            continue
    get_match_stats()

def get_match_stats():
    for x in match_id_list:
        try:
            index = 0
            match_stats = api.get_matchstats(x)
            time.sleep(1)
            while index < 10:
                sql = "INSERT INTO summonerstats (win, championId, item0, item1, item2, item3, item4, item5) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)"
                val = ((match_stats['participants'][index]['stats']['win']),
                       (match_stats['participants'][index]['championId']),
                       (match_stats['participants'][index]['stats']['item0']),
                       (match_stats['participants'][index]['stats']['item1']),
                       (match_stats['participants'][index]['stats']['item2']),
                       (match_stats['participants'][index]['stats']['item3']),
                       (match_stats['participants'][index]['stats']['item4']),
                       (match_stats['participants'][index]['stats']['item5']))
                cursor.execute(sql, val)
                index += 1
        except:
            index +=1
            continue
    mydb.commit()