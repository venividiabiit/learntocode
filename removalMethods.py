motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#
popped_motorcycles = motorcycles.pop()
# # will remove the last item in the list
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
#
# motorcycles.remove('ducati')
# print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for my tastes.")