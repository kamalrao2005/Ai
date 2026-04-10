from pyDatalog import pyDatalog

pyDatalog.clear()

pyDatalog.create_terms(
    'student, course, enrolled, prerequisite, eligible, '
    'advanced_student, not_eligible, X, Y, Z'
)

+ student('alice')
+ student('bob')

+ course('math101')
+ course('cs101')
+ course('cs201')

+ enrolled('alice', 'math101')
+ enrolled('alice', 'cs101')
+ enrolled('bob', 'math101')

+ prerequisite('cs101', 'math101')
+ prerequisite('cs201', 'cs101')

eligible(X, Y) <= enrolled(X, Z) & prerequisite(Y, Z)
advanced_student(X) <= enrolled(X, 'cs101')
not_eligible(X) <= student(X) & ~eligible(X, 'cs201')

print("Eligible students for courses:")
print(eligible(X, Y))

print("\nStudents eligible for cs201:")
print(eligible(X, 'cs201'))

print("\nAdvanced students:")
print(advanced_student(X))

print("\nStudents NOT eligible for cs201:")
print(not_eligible(X))
