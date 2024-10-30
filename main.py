# Alex Williams
# 10/30/2024
# Web and App Development

# Part 1

# Favorites

# favorite_things = ['Johnny Depp','Scarlet Johansson','Mount Rushmore','Florida','Funions','Cheetos puffs']

# print(favorite_things)

# The pop() Method

# favorite_things.pop()
# print(favorite_things)

# favorite_things.pop(2)
# print(favorite_things)


# The remove() method

# favorite_things.remove('Mount Rushmore')

# print(favorite_things)

# Keyword DEL

# del favorite_things[2]

# print(favorite_things)

# Part 2

dinner_guests = ['Johnny Depp','Julius Ceaser','Micheal Jackson','Queen Elizabeth','Jesus Christ']

print(f'Hello, {dinner_guests[0]} you are invited to my dinner party')
print(f'Hello, {dinner_guests[1]} you are invited to my dinner party')
print(f'Hello, {dinner_guests[2]} you are invited to my dinner party')
print(f'Hello, {dinner_guests[3]} you are invited to my dinner party')
print(f'Hello, {dinner_guests[4]} you are invited to my dinner party')

print(f"I'm sorry everybody but {dinner_guests[1]} cannot make it to the party")

dinner_guests.remove('Julius Ceaser')
print(dinner_guests)

print(f'Those who are still able to attend the dinner party are {dinner_guests[0]}, {dinner_guests[1]}, {dinner_guests[2]}, and {dinner_guests[3]}.')



print("I regret to infrom everyone that the table I rodered will not be coming in on time so I'll only have room for two guests")

dinner_guests.pop(1)

print('I am sorry Micheal Jackson but you are uninvited from the party')

dinner_guests.pop(1)

print('I am also sorry to you Queen Elizabeth but you are also reoved from the list')

print(dinner_guests)

print(f'{dinner_guests[0]} and {dinner_guests[1]}, you both are sill invited to the dinner party.')

del dinner_guests[1]
del dinner_guests[0]

print(dinner_guests)