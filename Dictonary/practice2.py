students= [
    {"Name " :  "Sahil", "School": "JJA", "Group": "A"},
    {"Name " :  "Manish", "School": "Friends", "Group": "B"},
    {"Name " :  "Tejas", "School": "VPM", "Group": "C"},
    {"Name " :  "Sahil Jadhav", "School": "ACADEMY", "Group": "D"}
]

for student in students: 
    print(student["Name "], student["School"], student["Group"], sep=": ")