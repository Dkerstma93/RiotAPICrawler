import itertools
from V_Database import mydb
import time
from V_Get_Summoners import api

cursor = mydb.cursor()

def get_match_stats():
    cursor.execute("select gameid from gameids")
    match_id_list = list(itertools.chain.from_iterable(cursor))
    for x in match_id_list:
        index = 0
        match_stats = api.get_matchstats(x)
        time.sleep(1)
        while index < 10:
            sql = "INSERT INTO summonerstats (win, championId, item0, item1, item2, item3, item4, item5) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)"
            val = ((match_stats['participants'][index]['stats']['win']),(match_stats['participants'][index]['championId']),(match_stats['participants'][index]['stats']['item0']),(match_stats['participants'][index]['stats']['item1']),(match_stats['participants'][index]['stats']['item2']),(match_stats['participants'][index]['stats']['item3']),(match_stats['participants'][index]['stats']['item4']),(match_stats['participants'][index]['stats']['item5']))
            cursor.execute(sql, val)
            index += 1
    mydb.commit()




