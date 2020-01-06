import itertools
from V_API import V_API
import time
from V_Database import mydb


api = V_API('RGAPI-12cdd90e-0577-48df-94a2-b09d8b2f4310') #Insert API key
cursor = mydb.cursor()

summoner_list = []
summoner_division_list = []
match_id_list = []
division_list = ['I']
tier_list = ['DIAMOND']

# fills summoner_list[] with summonersnames from each division and tier
def save_summoners():
    # for j in tier_list:
    #     for i in division_list:
    #         request_summoners = api.get_summoners('RANKED_SOLO_5x5',j,i)
    #         time.sleep(1)
    #         for x in request_summoners:
    #             summoner_list.append(x['summonerName'])
    #             summoner_division_list.append(j + ' ' + i)
    summoner_list.append('Geniepige Rat')
    summoner_division_list.append('DIAMOND I')
#Use summoner names to get encrypted summoner ids
def save_saccount_id():
    index = 0
    for x in summoner_list:
        try:
            request_summonerid = api.get_summoner_by_name(x)
            time.sleep(1)
            sql = "INSERT INTO summonernames (summonername, summonerid, division) VALUES (%s, %s, %s)"
            val = (x, request_summonerid['accountId'], summoner_division_list[index])
            cursor.execute(sql, val)
            index+=1
        except:
            index+=1
            continue
    mydb.commit()

# #Use account ids to request matchids
def save_match_id():
    cursor.execute("select summonerid from summonernames")
    summonerid_list = list(itertools.chain.from_iterable(cursor))
    for x in summonerid_list:
        request_matchids = api.get_match_history(x)
        time.sleep(1)
        index = 0
        try:
            for y in request_matchids['matches']:
                cursor.execute("INSERT INTO gameids (gameid) VALUES (" + str(request_matchids['matches'][index]['gameId']) + ")")
                index +=1
        except:
            index +=1
            continue
    mydb.commit()