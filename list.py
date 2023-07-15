friends = ["Kelvin", "Victor", "Blessing", "Elsie", "Emmanuel"]
print(friends)
print(friends[-1])
print(friends[1:3])
friends[2] = "Blessing"
print(friends[2])

#list functions
lucky_numbers = [42, 15, 8, 16, 23, 4]
friends = ["kelvin", "victor", "victor", "victor", "blessing", "elsie","emmanuel"]
friends.extend(lucky_numbers)
friends.append("Peter")
friends.insert(0, "charles")
friends.remove("kelvin")
friends.pop()
print(friends.index("elsie"))
print(friends.count("victor"))
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
friends2 = friends.copy()
print(friends2)
#so this is my first time experience learning list functions in python.
