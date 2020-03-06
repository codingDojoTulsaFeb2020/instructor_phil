x = [ [5,2,3], [10,8,9] ] 

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10}, {'y': 20} ]

# print(x[1][0])
# print(x)
# x[1][0] = 15
# print(x)

# students[0]['last_name'] = 'Bryant'
# print(students)

# print(type(sports_directory))
# print(type(sports_directory['soccer']))
# print(sports_directory['soccer'][0])
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)
# print(len(z))
# print(type(z[1]['y']))
# print(z[1]['y'])
# z[1]['y'] = 30
# print(z)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(student_list):
    print(len(student_list))
    print(type(student_list))
    for student in student_list:
        fname, lname = student.keys()
        # print(fname)
        # print(lname)
        # print(type(student))
        print(f'{fname} - {student[fname]}, {lname} - {student[lname]}')

# iterateDictionary(students)
def iterateDictionary2(student_list, key_name):
    for student in student_list:
        if key_name in student:
            print(student[key_name])

# iterateDictionary2(students, 'first_name')

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(locations):
    location, instructors = dojo.keys()
    print(f'{len(dojo[location])} {location.upper()}')
    for l in dojo[location]:
        print(l)
    print(f'{len(dojo[instructors])} {instructors.upper()}')
    for i in dojo[instructors]:
        print(i)
    # print(instructors)

printInfo(dojo)