universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats(universities):
    student_enrollment_value = []
    tuition_fees = []
    returned_list = []
    for list_ in universities:
        student_enrollment_value.append(list_[1])
        tuition_fees.append(list_[2])
    returned_list.append(student_enrollment_value)
    returned_list.append(tuition_fees)
    return returned_list


def mean(list_):
    return sum(list_) / len(list_)


def median(list_):
    sorted_list = sorted(list_)
    if len(sorted_list) % 2 != 0:
        mean_ = int((len(sorted_list) + 1) / 2 - 1)
        return sorted_list[mean_]
    else:
        number1 = int(len(sorted_list) / 2 - 1)
        number2 = int(len(sorted_list) / 2)
        return (sorted_list[number1] + sorted_list[number2]) / 2


star = "*"

students = [i[1] for i in universities]
tuition = [i[2] for i in universities]
total_student = sum(students)
total_tuition = sum(tuition)

student_mean = mean(students)
tuition_mean = mean(tuition)

student_median = median(students)
tuition_median = median(tuition)



print(star * 30)

print(f"Total students: {total_student}")
print(f"Total tuition: ${total_tuition:.2f}")
print("\n")
print(f"Student mean: {student_mean:.2f}")
print(f"Student median: {student_median}")
print("\n")
print(f"Tuition mean: ${tuition_mean:.2f}")
print(f"Tuition median: ${tuition_median:.2f}")

print(star * 30)

# print(enrollment_stats(universities))
