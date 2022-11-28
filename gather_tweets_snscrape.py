import os
from datetime import datetime, timedelta
start = datetime(2017, 2, 23)
end = datetime(2023, 4, 15)
delta = timedelta(days=1)

d = start
diff = 0
weekend = {5, 6}
while d <= end:
    if d.weekday() in weekend:
        d += delta
        continue

    since = d.strftime("%Y-%m-%d")
    d += delta
    until = d.strftime("%Y-%m-%d")

    command = f"snscrape --jsonl --progress --max-results 400 twitter-search --top \"(Elon Musk OR Musk) lang:en until:{until} since:{since} -filter:replies\" > elontweets\\{since}.jsonl"
    os.system(command)


# Using OS library to call CLI commands in Python
# os.system("snscrape --jsonl --max-results 500 --since 2020-06-01 twitter-search 'its the elephant until:2020-07-31' > text-query-tweets.json")


# Using OS library to call CLI commands in Python
#os.system("snscrape --jsonl --progress --since 2022-03-02 twitter-search \"Tesla until:2022-03-17 min_faves:100\" > text-query-tweets.json")

#os.system("snscrape --jsonl --progress --since 2022-03-02 twitter-search \"Tesla until:2022-03-17 min_faves:100\" > text-query-tweets.json")


#os.system("snscrape --jsonl --progress --max-results 300 twitter-search \"(tesla OR tsla) until:2013-04-16 since:2013-04-15 -filter:replies\"")
