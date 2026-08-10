students = ["Anu", "Ravi", "Priya", "Kiran"]
marks = [85, 72, 91, 68]

print("Students and Marks")

for i in range(len(students)):
    print(students[i], "-", marks[i])
    print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Average Marks:", sum(marks) / len(marks))