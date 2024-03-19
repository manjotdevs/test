'''
1. Add students
2. Show all students
3. Delete students
4. Exit
'''

print("1. Add students\n2. Show all students\n3. Delete students\n4. Exit")

a = int(input("=> "))

if a == 1:
   print("1.Add student to new class\n2.Add student to existing class") 
   b = int(input())
   if b == 1:
       list_name = input("Enter list name => ")
       added_students = input("Enter student => ")
       student_list = []
       student_list.append(added_students)
       print(f"file name {list_name}\n Students added are{student_list}")
       #print("file name",list_name,"\n Students added are",student_list)
         
    