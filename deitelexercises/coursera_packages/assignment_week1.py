dog_age = input("enter the dog year")
human_age_year_one = 15
human_age_year_two = 12
human_age_year_three = 9.3
human_age_year_four = 8
human_age_year_five = 7.2
dog_to_human_age = 0
try:
    # dog_age = int(dog_age)
    dog_age = float(dog_age)

    if dog_age == 1:
        dog_to_human_age = dog_age * human_age_year_one
    elif dog_age == 2:
        dog_to_human_age = dog_age * human_age_year_two
    elif dog_age == 3:
        dog_to_human_age = dog_age * human_age_year_three
    elif dog_age == 4:
        dog_to_human_age = dog_age * human_age_year_four
    elif dog_age <= 5:
        dog_to_human_age = dog_age * human_age_year_five
    else:
        dog_to_human_age = (5 * 7.2) + ((dog_age - 5) * 7)
    print(f'The given dog age {dog_age} is {dog_to_human_age: .2f} in human years')

except ValueError as e:
    print("invalid input")



