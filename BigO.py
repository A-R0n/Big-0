# Python 3.7
# Big O Notation examples of functions with constant, linear, and quadratic time complexity

import time


trees = ['oak', 'sequoia', 'pine', 'beach', 'palm', 'boddhisatva', 'maple']
treeFacts = [['oak', 3], ['palm', 1], ['palm', 2], ['beach', 5], ['maple', 7]]

# constant time complexity --> O(1)
def dumbFunction(x):
    emptyBox = 0
    print(emptyBox)

# linear time complexity --> O(n)
def linearComplexity(x):
    for tree in x:
        print(tree)

# quadratic time complexity --> 0(N squared)
def quadraticComplexity(x):
    start = time.time()
    for sale in x:
        for description in sale:
            if description == 7:
                end = time.time()
                print(end-start)
            else:
                continue

dumbFunction(trees) # 0
linearComplexity(trees) # oak, sequoia, pine, beach, palm, boddhisatva, maple
quadraticComplexity(treeFacts) # how long will it take to find the correct receipt?

