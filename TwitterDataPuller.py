

import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

import os


# Creating list to append tweet data to
# tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
# for i,tweet in enumerate(tqdm(sntwitter.TwitterSearchScraper('$MSFT since:2019-01-01 until:2022-11-12 lang:en').get_items())):
#  if i>500:
# break

# if tweet.user.followersCount>20000:
# tweets_list2.append([tweet.date, tweet.id, tweet.content,tweet.retweetCount,tweet.user.followersCount,tweet.likeCount ,tweet.user.username,])

# Creating a dataframe from the tweets list above
# tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text',"Retweet Count","Followers","likes", 'Username'])

def twitter_stock_puller(stock_name, date_from, date_to):
    tweets_list2 = []
    N = 200000

    if not os.path.exists(f"{stock_name}"):
        os.makedirs(f"{stock_name}")

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(
            f'{stock_name} since:{date_from} until:{date_to} lang:en min_faves:35').get_items()):
        if tweet.user.followersCount > 10000:
            if len(tweets_list2) > 5000:
                break
            else:
                tweets_list2.append([tweet.date, tweet.id, tweet.content.replace("\n", ""), tweet.retweetCount,
                                     tweet.user.followersCount, tweet.likeCount, tweet.user.username, ])




    # Creating a dataframe from the tweets list above
    tweets_df2 = pd.DataFrame(tweets_list2,
                              columns=['Datetime', 'Tweet Id', 'Text', "Retweet Count", "Followers", "Likes",
                                       'Username'])
    tweets_df2.to_csv(f"{stock_name}/{stock_name}-({date_from}-{date_to}).csv")

    print(f"{stock_name} done")





t = np.arange(datetime(2019,1,1), datetime(2022,11,12), timedelta(days=28)).astype(datetime)
l = []
for ix in t:
  l.append(ix.strftime("%Y-%m-%d"))

for i in ['$AMZN' , '$MSFT' , '$GOOGL', '$AAPL']:

  for x in range(len(l)-1):

    start_date = l[x]
    end_date = l[x+1]



    twitter_stock_puller(stock_name=i,date_from=start_date, date_to=end_date)

