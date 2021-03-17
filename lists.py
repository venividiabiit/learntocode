bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# this will print out the [] also.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
# will return the 1st item with Capitalized.
print(bicycles[-1])
# a -1 will return the last item. sometimes it is only necessary to return the last item.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = 'My first bicycle was a ' + bicycles[0].title() + "."
print(message)
# 3.1
names = ['berry', 'benjamin', 'taco', 'robert', 'joshua']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())
# 3.2
print(f'Hello there, {names[0].title()}' + '!')
print(f'Hello there, {names[1].title()}' + '!')
print(f'Hello there, {names[2].title()}' + '!')
print(f'Hello there, {names[3].title()}' + '!')
print(f'Hello there, {names[4].title()}' + '!')
# 3.3
vehicles = ['yamaha', 'ferrari', 'honda', 'porsche']
print(f'I would like to own a {vehicles[1].title()} sportscar.')

'''
What is the difference between an array and a list?
Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.
^ from W3schools.com
'''

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles[0] = 'ducati'
# will remove element honda and replace it with honda.
# print(motorcycles)
# appending elements.
motorcycles.append('ducati')
print(motorcycles)
# this will append the item ducati to the list, without modifying the other elements.
# the append method  is for easily building dynamic lists.
motorcycles = []

motorcycles.append('honda')
motorcycles.append('suzuki')
motorcycles.append('yamaha')
print(motorcycles)

popp