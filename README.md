smarkets
===============

Interview Exercise


These are the apis available with description:

/users :- Shows all users
/affiliates :- Shows all affiliates
/bets/{betId} :- Data about betId. Sample betId: 111
/affiliates/{affiliate_id} :- Data about affiliateId. Sample affiliateId: 8
/users/{userId} :- Data about userId. Sample userId: 1
/users/{userId}/bets :- All bets by userI


Interview Questions:

Find the affiliate with the maximum number of users.
Find the amount won by users coming through the top 3 affiliates - by user_count.
What is the percentage of users who have won 2 or more bets with low odds - say 25%.
To call an api append the route given to the current url: For example: smarkets.herokuapp.com/users Calls the /users route.