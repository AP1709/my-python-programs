# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
a=0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
for i in range (0,len(student_heights)):
  a=a+student_heights[i]
print("avg height is",int(a/len(student_heights)))


#Write your code below this row 👇




