    ##Create a new dictionary called prices using {} format like the example above.
    ##Put these values in your prices dictionary:
    ##"banana": 4,
    ##"apple": 2,
    ##"orange": 1.5,
    ##"pear": 3

prices = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3

}


    ##And these values in your stock dictionary:
    ##    "banana": 6
    ##    "apple": 0
    ##    "orange": 32
    ##    "pear": 15

stock = {
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15

}

    ##Loop through each key in prices. For each key, print out the key along with
    ##its price and stock information. Print the answer in the following format:
    ##apple
    ##price: 2

for k in prices:
    print (k)
    print ("price: {0}".format(prices[k]) )
    print ("stock: {0}\n".format(stock[k]) )


##Let's determine how much money you would make if you sold all of your food.
    
##Create a variable called total and set it to zero.
total = 0

##Loop through the prices dictionaries.For each key in prices, multiply the number in
##prices by the number in stock. Print that value into the console and then add it to total.
for k  in prices:
    money = prices[k] * stock [k]
    print ("Money from selling {0}: {1}".format (k, money) )
    total += money

##Finally, outside your loop, print total.
print ( "\nMoney that I would make if i sold all of my foods: {0}".format(total) )

