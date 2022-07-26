# number = 5
# lots_of_numbers = [number for number in range(5,50)]
# print(number)
# print(lots_of_numbers)

user_access_details = [{"Username": "Yemisi", "Password": "1234"},
                       {"Username": "Simi", "Password": "0000"},
                       {"Username": "Sharon", "Password": "1111"}]


def validate_username(Username, password):
    for User in user_access_details:
        if User["Username"] == Username and User["Password"] == password:

            return True
    return False
user_details = {
    "favourite_food": ["rice","beans","dodo"],
    "favourite_players": {"Arsenal":"Bukayo", "Chelsea":"Lukaku", "Dekanorbs": "Ladi"},
    "favourite_girl": "Simi",
    "favourite_music": ["Buga","last last","italy"],
    "favourite_language": {"programming":"python", "Dialect":"Yoruba","Slang":"breakfast"}

}

def type_checker(types):
    # return [val for val in user_details.values() if type(val) == types]
    l =[]
    for value in user_details.values():
        if type(value) == types:
            l.append(value)
    return l

contact_details ={
    "fullname": "Ismail Oluwayemisi",
    "phonenumber": ["07062396366"],
    "address" : ["shomolu","bariga","egbeda"],
    "school": {"semicolon","lasu"}
}

def add_list(phonenumber):
    for key, val in contact_details.items():
        if key == "phonenumber" and type(val) == list:

            return val.append(phonenumber)



if __name__ == "__main__":
    add_list("09075586677")
    print(contact_details)
