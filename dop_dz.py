grades = [[5, 3, 3, 5, 4],[2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_ = sorted(list(students))
average_rating = dict([])
average_rating.update({students_[0]: sum(grades[0])/len(grades[0]), students_[1]: sum(grades[1])/len(grades[1]),
                       students_[2]: sum(grades[2])/len(grades[2]),students_[2]: sum(grades[2])/len(grades[2]),
                       students_[3]: sum(grades[3])/len(grades[3]),students_[4]: sum(grades[4])/len(grades[4]),
                       students_[4]: sum(grades[4])/len(grades[4])})
print(average_rating)


#-------------------------------------------------------------------------------------

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(list(students))

def calculate_average(grades):
    return sum(grades) / len(grades)

student_avg_dict = dict([])
for student in students:
    index = students.index(student)
    avg_grade = calculate_average(grades[index])
    student_avg_dict[student] = round(avg_grade, 2)

print(student_avg_dict)



