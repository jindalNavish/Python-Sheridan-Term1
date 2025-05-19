subject = ["python","maths","web"]
grades = [95, 89, 100]
end_list = subject.extend(grades)
print(subject)
subject_remove = "python"

if subject_remove in subject:
    subject_index = subject.index("python")
    subject.pop(subject_index)
    garde_index = subject_index + 2
    grade_index_ok = subject_index
    grades.pop(subject_index)
    subject.pop(garde_index)
print(subject)

subject_remove = "Technical"
if subject_remove not in subject:
    subject.insert(2,subject_remove)
    subject.append(85)
    grades.append(85)
print(subject)

average = sum(grades)/3
new_list = []
new_list.extend(subject)
new_list.append(average)
print(new_list)

if average >= 90:
    print("You achieved Grade A")

elif average >= 80:
    print("You achieved Grade B")

elif average >= 70:
    print("You achieved Grade C")

elif average >= 60:
    print("You achieved Grade D")
    
else:
    print("fail")