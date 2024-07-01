# -------------------- Sets ---------------------------

mySet = {"banana", "mango", "apple", "orange", "pineapple"}
set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
x= [10, 11, 13, True]
y = {2, 4, 6, 8, 10, 12, 16, 18, 20}
set3 = set2 | y
print(set3)

# ------------------ Dictionary --------------------------
myDict = {"name": "Ikenna", "age": 20, "institution": "FUNAI", "graduationYear": 2021, "isStudent": False, "skill":["HTML", "CSS", "JS", "C#", "JAVA", "PYTHON"]}
print(myDict["skill"])
skill = myDict.get("skill")
print(skill)
print(myDict.keys())
print(myDict.values())
print(myDict.items())
[print(myDict["age"]) if "age" in myDict else printL("Age not in the object")]

for x in myDict:
    print(f"{x} : {myDict[x]}")
[print(f"{x} : {myDict[x]}") for x in myDict]