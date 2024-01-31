student={}
for i in range (1,3):
	print("Enter student name and obtain marks")
	name=input()
	obtain_marks=input()
	student[i]={'name':name, 'obtain_marks':obtain_marks}
	student[name] = obtain_marks
	
		 	 
n= input('Enter Student Name: ')
if n in student.keys():
	print(student[n])
else:
	print('Student Data Not Found')