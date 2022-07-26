from functools import reduce
from statistics import mean

feeds = [{"Username":"Holuwayhemisi", "age":30, "tweets":["i'm new here","i'm hungry", "please follow me"],"verified": "False" },
         {"Username":"Simisanyaa", "age":22, "tweets":["i'm blessed","Hey fans"],"verified": "True" },
         {"Username":"Drpampam", "age":28, "tweets":["Buhari's government is useless","Who's ready for giveaway", "Advertise your brand"],"verified": "True" },
         {"Username":"Akinloye", "age":35, "tweets":["Education is key","Your politicians are thieves"],"verified": "True" },
         {"Username":"Linda", "age":21, "tweets":["i'm new here","i'm looking for husband", "please follow me"],"verified": "False" },
         {"Username":"Seun", "age":25, "tweets":[],"verified": "false" },
         {"Username":"Wesley", "age":29, "tweets":[],"verified": "false" },
         {"Username":"Nkechi", "age":25, "tweets":["I sell beautiful slides", "please follow me"],"verified": "False" },
         {"Username":"Gistloversblog", "age":30, "tweets":["linda ikeji welcomes a boy"],"verified": "True" },
         {"Username":"Hausagirl", "age":22, "tweets":["men are scum","relationship is not for everyone", "i'm lonely"],"verified": "False" },
         ]
print("Usernames of all twitter users: ")
print([feed["Username"] for feed in feeds])
print()

print("usernames of active users:  ")
print([feed["Username"] for feed in feeds if feed["tweets"] != []])
print()


print("username of verified users below the age of 25: ")
print([feed["Username"] for feed in feeds if feed ["age"] <= 25 and "True" in feed["verified"]])
print()


print("username of verified users:")
print([feed["Username"] for feed in feeds if feed["verified"] == "True"])
user= map(lambda y:y['Username'], filter(lambda x: x["verified"],feeds))
print("using map and filter, the username of the verified users are: ",user)
print()


print("the maximum age is:")
maxi = reduce(lambda x, y: x if x["age"] > y["age"] else y, feeds)
maximum = (max(feed["age"] for feed in feeds))
print(maxi)
print("using list comprehension, the maximum is:",maximum)
most_tweets = max(feeds,key=lambda feed: len(feed["tweets"]))["tweets"]
print("getting the maximum of tweets",most_tweets)
print()

print("the minimum of the age is: ")
mini =reduce(lambda x,y: x if x["age"] < y["age"] else y,feeds)
print("The minimum using reduce: ",mini)
minimum = (min(feed["age"] for feed in feeds))
print("the minimum using list comprehension is: ",minimum)
print()

# average = ((sum(feed["age"]for feed in feeds)) /  len["age"])
# print("the minimum is: ",average)

average = reduce(lambda x, y: x+y, (feed ["age"] for feed in feeds)) / len(feeds)
print("the average is:", average)

avg= sum(feed["age"] for feed in feeds)/ len(feeds)
print("the avg: ",avg)
print(mean(feed["age"] for feed in feeds))
print()

lst = list((feed["age"] for feed in feeds))
print("the age of all the users are: ",lst)


print("sorting the name from ascending order: ")
print(sorted(feeds,key=lambda x: x["Username"]))
print()


print("sorting the name in a descending order:")
print(sorted(feeds,key=lambda x: x["Username"],reverse=True))
print()

print("sorting the age ")
print(sorted(feeds,key= lambda x: x["age"]))
print()


longest = reduce(lambda x,y: x if len(x["Username"]) >= len(y["Username"]) else y,feeds )
print("the longest is: ",longest)
print("the longest is: ",longest["Username"])