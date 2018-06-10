inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory ["pocket"] = ['strange berry', 'seashell', 'lint']
print(*inventory["pocket"], sep=",")
del inventory['backpack'][1]
print(*inventory['backpack'], sep=",")
inventory["gold"] += 50
print(inventory["gold"])