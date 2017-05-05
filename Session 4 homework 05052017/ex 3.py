##Follow the steps:
##    First, make a list called groceries with the values "banana","orange", and "apple".
groceries = [ "banana","orange", "apple" ]
x = ", ".join(groceries)
print ("The grocery store has {0}\n".format(x) )

##    Define this two dictionaries:
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

##    Define a function compute_bill that takes one argument food as input. In the function,
##    create a variable total with an initial value of zero.
##    For each item in the food list, add the price of that item to total.
##    Finally, return the total. def compute_bill (food)
##  Ignore whether or not the item you're billing for is in stock.
##  Note that your function should work for any food list.
def compute_bill (food):
    total = 0
    for i in food:
        total += prices[i]
    return total

a = compute_bill (groceries)
print ("Total price of all items: {0}".format(a) )


##    Make the following changes to your compute_bill function:
##    While you loop through each item of food,
## only add the price of the item to total if the item's stock count is greater than zero.
##    If the item is in stock and after you add the price to the total,
## subtract one from the item's stock count.

def compute_bill2 (food):
    total = 0
    for i in food:
        if stock [i] > 0:
            total += prices[i]
    return total

b = compute_bill2 (groceries)
print ("Total price of all items that has stock count greater than zero: {0}".format(b) )

