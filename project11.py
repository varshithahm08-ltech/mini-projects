all_subjects = ("Python", "Java", "DBMS", "OS", "Web")

completed = {"Python", "DBMS", "Web"}

pending = set(all_subjects) - completed

print("All Subjects:", all_subjects)
print("Completed:", completed)
print("Pending:", pending)