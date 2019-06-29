from sklearn import tree
import numpy as np

#features = [[155, "rough"], [180, "rough"], [135, "smooth"], [110, "smooth"], [120, "smooth"], [250, "smooth"], [220, "smooth"]]
#labels = ["orange", "orange", "apple", "apple", "apple", "mango", "mango"]

features = [[155, 0], [180, 0], [135, 1], [110, 1], [120, 1], [250, 1], [220, 1]]
labels = [1, 1, 0, 0, 0, 2, 2]

classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(features, labels)
x = input("Weight of the fruit in gm?: ")
y = input("Texture of the fruit? (put 1 if smooth 0 otherwise): ")
#x = 130;
#y = 0;
test = [x, y]
result = (classifier.predict([test]))
#print (classifier.predict([test]))

def printFruitName(int):
    if result == [2]:
        print ("It's a Mango!!")
    elif result == [0]:
        print ("It's an Apple!!")
    elif result == [1]:
        print ("It's an Orange!!")

printFruitName(result)
        
       