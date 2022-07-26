# using zip
student_1 = [45,67,98]
student_2 =[56,87,52]
student_3 =[61,43,44]

print(list(zip(student_1,student_2,student_3)))

# to form a dictionary, use dict
print(dict(zip(student_1,student_2,)))

sum_per_subject = []
scores =[max(subject) for subject in zip(student_1,student_2,student_3)]
score =[sum(subject) for subject in zip(student_1,student_2,student_3)]
print("the sum is: ",score)
print("the max is: ",scores)


# using slice
s =  "Hello"

print(s[1:3])

s_slice = slice(1,4)
print("Hello"[s_slice])

