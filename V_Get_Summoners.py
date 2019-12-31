from V_API import V_API
import time


api = V_API('RGAPI-8ae61627-2df0-46a4-a39e-ae5e9bf8b2f6') #Insert API key


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
            time.sleep(1.3)
            for x in request_summoners:
                summoner_list.append(x['summonerName'])

#Use summoner names to get encrypted summoner ids
def save_saccount_id():
      for x in summoner_list:
        try:
            request_summonerid = api.get_summoner_by_name(x)
            time.sleep(1.3)
            account_id_list.append(request_summonerid['accountId'])
        except:
            continue


#Use account ids to request matchids
def save_match_id():
    for x in account_id_list:
        try:
            request_matchids = api.get_match_history(x)
            time.sleep(1.3)
            index = 0
            for y in request_matchids['matches']:
                if y not in match_id_list:
                    match_id_list.append(request_matchids['matches'][index]['gameId'])
                    index += 1
        except:
            continue



