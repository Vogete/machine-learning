from sklearn import tree

features = [[135,0], [130, 0], [150, 1], [170, 1]]

labels = [0,0,1,1]

clf= tree.DecisionTreeClassifier()

clf = clf.fit(features, labels)

print (clf.predict([[160, 1]]))
