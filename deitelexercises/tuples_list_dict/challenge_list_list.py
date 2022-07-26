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
    student_values = []
    tuition_fees = []
    returned_value = []

    for list_ in universities:
        student_values.append(list_[1])
    for list_ in universities:
        tuition_fees.append(list_[2])
    returned_value.append(student_values)
    returned_value.append(tuition_fees)
    return returned_value

def mean_(numbers):
    return sum(numbers)/len(numbers)

def median_(list_):
    sorted_list = sorted(list_)
    if len(sorted_list) % 2 != 0:
        mediian = int((len(sorted_list) + 1) / 2 - 1)
        return sorted_list[mediian]
    else:
        num1 = int(len(sorted_list))/2 - 1
        num2 = int(len(sorted_list)/2)
        return (sorted_list[num1] + sorted_list[num2])/2


students = [student[1] for student in universities]
tuition_fees = [tuition[2] for tuition in universities]


total_students = sum(students)
total_tuition = sum(tuition_fees)

student_mean = mean_(students)
student_median = median_(students)

tuition_mean = mean_(tuition_fees)
tuition_median = median_(tuition_fees)


print(f"Total students: {total_students}")
print(f"Total tuition: ${total_tuition}")
print("\n")

print(f"Student mean: {student_mean}")
print(f"Student median: {student_median}")
print("\n")

print(f"Tuition mean: {tuition_mean}")
print(f"Tuition median: {tuition_median}")