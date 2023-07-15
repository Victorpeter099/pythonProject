#tuples in python
coordinates = [(4, 5), (6, 7), (74, 30), (16, 18)]
print(coordinates[-1])

house_hold = ['ngozi', 'victor', 'elsie', 'emma', 'christy', 'peter']
print('victor' in house_hold)
for item in house_hold:
    print(item)
courses = ['biology', 'maths', 'chemistry', 'physics', 'anatomy']

for index, course in enumerate(courses, start=1):
    print(index, course)

courses = ['biology', 'maths', 'chemistry', 'physics', 'anatomy']
course_str = '- '.join(courses)
new_list = course_str.split(' - ')
print(course_str)
print(new_list)

# Mutable
list_1 = ['arts', 'government', 'account', 'english']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'agric'

print(list_1)
print(list_2)



# Immutable
tuple_1 = ('arts', 'government', 'account', 'english')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'soil science'

print(tuple_1)
print(tuple_2)

# Sets
cs_courses = {'history', 'maths', 'physics', 'biology'}
art_courses = {'design', 'maths', 'english', 'biology'}
print(cs_courses.union(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.intersection(art_courses))
print(cs_courses)
print('biology' in cs_courses)

#Empty list
empty_list = []
empty_list = list ()

#Empty tuples
empty_tuples = ()
empty_tuples = tuple()

#Empty set
empty_set = {} # this is not right but a dict
empty_set = set()
