    #Given the following dictionary:
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}


    ##Add a key to inventory called 'pocket'.
    ##Set the value of 'pocket' to be a list consisting of the strings
    ##'seashell', 'strange berry', and 'lint'.
inventory ['pocket'] = [ 'seashell', 'strange berry', 'lint' ]

    ##.sort()the items in the list stored under the 'backpack' key.
inventory['backpack'] .sort()

    ##Then .remove('dagger') from the list of items stored under the 'backpack' key.
inventory['backpack'].remove ('dagger')

    ##Add 50 to the number stored under the 'gold' key.
inventory['gold'] += 50
