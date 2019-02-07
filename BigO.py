

trees = ['oak', 'sequoia', 'pine', 'beach', 'palm', 'boddhisatva', 'maple']
treeFacts = [['oak', 7], ['palm', 1], ['palm', 2], ['beach', 5], ['maple', 2]]

def dumb_function(trees):
    emptyBox = 0
    return emptyBox


def linear_complexity(trees):
    for i in trees:
        print(i)
    


def quadratic_complexity(treeFacts):
    for tree in treeFacts:
        for purchase in tree:
            if purchase[1] == 1:
                receipt = purchase[0]
            if receipt == 'oak':
            print(receipt)
        

