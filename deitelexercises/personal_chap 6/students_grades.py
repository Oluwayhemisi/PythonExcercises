grade_book = {'Grace': [30, 50, 72],
              'Helen': [50, 60, 89],
              'Harry': [77, 89, 90],
              }
all_grades_total = 0
all_grade_count = 0
for name, grade in grade_book.items():
    total = sum(grade)
    print(total)
    print(f'Average for {name} is {total/len(grade): .2f}')
    all_grades_total += total
    all_grade_count += len(grade)
print(f'the class average is {all_grades_total/all_grade_count: .2f}')

