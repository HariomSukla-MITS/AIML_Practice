student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA"
}
print("Original Dictionary:", student)

print("Student Name:", student["name"])

student["city"] = "Bhopal"
print("After Adding:", student)

student["age"] = 21
print("After Updating:", student)

del student["course"]
print("After Removing:", student)

print("Dictionary Items:")
for key, value in student.items():
    print(key, ":", value)