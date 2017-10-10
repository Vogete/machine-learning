from sklearn import tree

def MakeChange(amount):
    count = 0
    occurence = 0
    coins = [100, 50, 20, 10, 5, 1]

    if amount > 0 :
        for i in range(0, len(coins)):
            occurence = amount // coins[i]
            amount -= occurence * coins[i]
            count += occurence

    return count


features = []
labels =[]

for money in range(1, 50000):
    change = MakeChange(money)

    _fchange = [change]
    _fmoney = [money]

    features.append(_fmoney)
    labels.append(_fchange)


clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

while True:
    print("add an input:")
    userinput = input()
    _predict = [[userinput]]
    answer = clf.predict(_predict)
    print(answer)

