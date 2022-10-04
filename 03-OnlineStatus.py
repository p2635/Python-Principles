# Online Status (https://pythonprinciples.com/challenges/Online-status/)
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

def online_count(dict):
    onlineCount = 0
    for status in dict.values():
        if status == "online":
            onlineCount += 1
        else:
            pass
    return onlineCount
    
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

print(online_count(statuses))
