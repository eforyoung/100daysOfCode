student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0

for height in student_heights:
    total_height += height
print(f"total_height = {total_height}")

number_students = 0
for students in student_heights:
    number_students += 1
print(f"number_student = {number_students}")

average_height = round(total_height/number_students)
print(f"average_height = {average_height}")
