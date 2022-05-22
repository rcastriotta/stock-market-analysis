import json

# Opening JSON file
f = open('data.json')

# returns JSON object as
# a dictionary
data = json.load(f)

largest = 0
for ticker in data:
    arr = data[ticker]
    if len(data[ticker]) != 254:
        continue
    for t in data:
        arr2 = data[t]
        score = 0
        start_amount = 10000
        daily_bet_amount = 1000
        money = start_amount
        if (t == ticker):
            continue
        if len(arr2) != 254:
            continue
        offset = 3
        for i in range(len(arr) - offset * 2):
            if arr[i] < arr[i + offset]:
                if (arr2[i + offset] < arr2[i + offset * 2]):
                    score += 1
                money -= daily_bet_amount
                money += (daily_bet_amount /
                          arr2[i + offset]) * arr2[i + offset * 2]

            if arr[i] > arr[i + offset]:
                if (arr2[i + offset] > arr2[i + offset * 2]):
                    score += 1

        if score > largest:
            largest = score
            print(ticker + " - " + t + " " +
                  str(score) + "/254" + " $" + str(int(money - start_amount)))
