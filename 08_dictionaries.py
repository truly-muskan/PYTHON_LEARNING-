# Example 1
student = {"name": "John", "age": 21}
print(student)

# Example 2
print(student["name"])

# Example 3
student["course"] = "Python"
print(student)

# Example 4
for key in student:
    print(key)

# Example 5
for key, value in student.items():
    print(key, value)