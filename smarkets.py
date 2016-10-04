# File name: smarkets.py
# Author: Emmanuel Osimosu
# Date created: 28/09/2016
# Python Version: 2.7

import urllib2
import json

# Base url of the API
urlbase = "http://smarkets.herokuapp.com/"

response = urllib2.urlopen(urlbase + 'users')
users = json.loads(response.read())
response = urllib2.urlopen(urlbase + 'affiliates')
affiliates = sorted(json.loads(response.read()), key=lambda a: a["id"])
affiliate_count = [[a["id"], 0] for a in affiliates]
# Let's count the number of users in each affiliate
for p in users:
    id = p["affiliate_id"]
    affiliate_count[id][1] += 1
# Let's sort the affiliate_count array to find the maximal count (for task 1) and top 3 affiliates (for task 2)
affiliate_count = sorted(affiliate_count, key=lambda x:-x[1])
max_aff = affiliates[affiliate_count[0][0]]
print "1. The affiliate", max_aff["name"], "with id", max_aff["id"], "and website", max_aff["website"], "has the maximal number of users (" + str(affiliate_count[0][1]) + " users)."

# ids of top 3 affiliates
top3 = [a[0] for a in affiliate_count[:3]]
# users are already loaded, so no need to call the API again
amount_won = 0
users_who_won_low_odd_bets = 0
for user in users:
    response = urllib2.urlopen(urlbase + 'users/' + str(user["id"]) + "/bets")
    bets = json.loads(response.read())
    low_odds_won = 0
    # Look for bets with result = true and odds <= 25%
    for bet in bets:
        if bet["result"] and bet["percentage_odds"] <= 25:
            low_odds_won += 1
    # If there are at least two such bets, this user qualifies for part 3
    if low_odds_won >= 2:
        users_who_won_low_odd_bets += 1
    if not user["affiliate_id"] in top3:
        # Skip users not from top 3 affiliates
        continue
    for bet in bets:
        # I assume the following meaning of the data:
        # "amount" is how much money the user bet
        # "result" indicates whether he won or lost
        # If the result is false, then the user loses his bet, hence his winnings are -amount
        # "percentage_odds" shows the odds of the user's victory, and winnings are proportional to the odds
        # Hence if the user won the bet, he gets his bet amount multiplied by the odds coefficient
        # Odds coefficient = 100 / percentage_odds, i.e. if percentage_odds = 25%, the user gets
        # amount * 100 / 25 = amount * 4, and his win is amount * 3 in addition to the money he bet
        if bet["result"]:
            amount_won += bet["amount"] * (100.0 / float(bet["percentage_odds"]) - 1)
        else:
            amount_won -= bet["amount"]
            
print "2. Amount won by the users of the top three affiliates is ", amount_won

print "3. The number of users who won two or more bets with odds <=25% is", users_who_won_low_odd_bets, "which amounts to", float(users_who_won_low_odd_bets)/float(len(users)) * 100.0, "percent of all users."