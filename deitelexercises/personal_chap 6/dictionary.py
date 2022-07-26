country_codes = {'finland': 'fi', 'south africa': 'za', 'nepal': 'np'}
print(len(country_codes))
if country_codes:
    print('country code is empty')

roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'IV': 4}
print(roman_numerals['III'])
roman_numerals['III'] = 8
print(roman_numerals)
del roman_numerals['III']
print(roman_numerals)
print(roman_numerals.get('II'))

# dictionary method keys and values

months = {'january': 1, 'february': 2, 'march': 3}
for month in months.keys():
    print(month, end=" ")

for month_num in months.values():
    print(month_num, end=" ")

months_view = months.keys()
for key in months_view:
    print(key, end=' ')

months['December'] = 12
print(months)

print(list(months.keys()))

for month in sorted(months.keys()):
    print(month)


# Dictionary method update
months_update = {}
months_update.update({"january": 1})
months_update.update({"february": 2, "march": 3, "April": 4})
print(months_update)

# Dictionary comprehension
months = {'january': 1, 'february': 2, 'march': 3}
months2 = {number: name for name, number in months.items()}
print(months2)

grades = {"sue": [98, 87, 94], "bob": [84, 95, 91]}
grades = {k: sum(v)/len(v) for k, v in grades.items()}
print(grades)
