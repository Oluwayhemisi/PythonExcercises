capitals = {
    "California": "Sacramento",
    "New York": "Albany",
    "Texas": "Austin",
}
print(capitals["Texas"])
capitals["colorado"] = "Denver"
print(capitals)

capitals["Texas"] = "Houston"
print(capitals)

del capitals["colorado"]
print(capitals)

for key in capitals:
    print(key)

for state in capitals:
    print(f"the capital of {state} is {capitals[state]}")
    
print(capitals.items())