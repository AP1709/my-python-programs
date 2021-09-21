# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
a=0
for i in range(0,len(student_scores)):
  if student_scores[i]>a:
    a=student_scores[i]
print("The highest score in class is",a)




