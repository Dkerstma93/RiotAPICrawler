import itertools
from V_API import V_API
import time
from V_Database import mydb


api = V_API('RGAPI-bc5f9e3d-a63c-4624-9db1-d533f33f417c') #Insert API key
cursor = mydb.cursor()

summoner_list = []
account_id_list = []
match_id_list = []
division_list = ['IV','III','II', 'I']
tier_list = ['IRON','BRONZE', 'SILVER', 'GOLD', 'PLATINUM', 'DIAMOND']

# fills summoner_list[] with summonersnames from each division and tier
def save_summoners():
     for j in tier_list:
         for i in division_list:
            request_summoners = api.get_summoners('RANKED_SOLO_5x5',j,i)
            time.sleep(1)
            for x in request_summoners:
                sql = "INSERT INTO summonernames (summonername, division) VALUES (%s,%s)"
                val = (x['summonerName'],j + ' ' + i)
                cursor.execute(sql, val)
     mydb.commit()

#Use summoner names to get encrypted summoner ids
def save_saccount_id():
    cursor.execute("select summonername from summonernames")
    summoner_list = list(itertools.chain.from_iterable(cursor))
    for x in summoner_list:
        try:
            request_summonerid = api.get_summoner_by_name(x)
            time.sleep(1)
            account_id_list.append(request_summonerid['accountId'])
        except:
            continue


# #Use account ids to request matchids
# def save_match_id():
#     for x in account_id_list:
#         request_matchids = api.get_match_history(x)
#         time.sleep(1)
#         index = 0
#         try:
#             for y in request_matchids['matches']:
#                 if y not in match_id_list:
#                     match_id_list.append(request_matchids['matches'][index]['gameId'])
#                     index += 1
#         except:
#             index +=1
#             continue
#


