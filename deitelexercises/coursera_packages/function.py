def say_something_specific(thing_to_say):
    print(thing_to_say)

say_something_specific("Hello world")


def number_sum(num1, num2):
    sum = num1 + num2
    print("The sum is: ",sum)
    return sum

a = 5
b = 3

result = number_sum(a,b)


def get_factors(x):
    factors_ = []
    for i in range(1, x+1):
        if x % i == 0:
            factors_.append(i)
    return factors_


print(get_factors(21))


def get_factors_(x):
    return[i for i in range (1, x+1)  if x % i == 0]
print(get_factors_(21))


list_ = [1,2,3,3,5,5,4,6,7]

def unique_list(x):
    get = []
    for i in x:
        if i not in get:
            get.append(i)
    return get

print(unique_list(list_))



def check_vowel(string):
    vowel_count = 0
    for char in string:
        if char in "aeiou":
            vowel_count +=1
    return vowel_count


print(check_vowel("dfghjkuytr"))



def word_counter(sentence):
    sentence = sentence.strip()
    word_count = 0
    for char in sentence:
        if char in ' ':
            word_count += 1
    return word_count

print(word_counter("d f gt tyc nbnvb"))


# def main():
#     while 1 == 1:
#         input_string = input("please give me a string ")
#         if input_string == '-1':
#             break
#         print(check_vowel(input_string), "vowels in", input_string)
#


def main():
    while 1 == 1:
        input_string = input("please enter a string \n ")
        if input_string == '-1':
            break
        print(word_counter(input_string), "words in", input_string)

if __name__ == '__main__':
    main()
