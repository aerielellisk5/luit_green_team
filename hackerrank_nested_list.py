python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# organize the list so that the scores arrange from lowest to highest

organized_list = []
countA = 0
countB = 0 

for student in python_students:
    # print((student[1]))
    if len(organized_list) == 0:
        organized_list.append(student)
    else:
        for grade in organized_list:
            # if student[0] > grade[0]:
                print(student[0])
                print(grade[0])
                
            #     organized_list.append(grade)
            #     student.pop(0)
            # else:    
            #     organized_list.insert(0, grade)
            #     student.pop(0)
            #     print(organized_list)
                
                
            
            
                
            