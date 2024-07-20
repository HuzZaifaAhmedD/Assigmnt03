# Assigmnt03

# Get user input for marks of 3 subjects
subject1_marks = float(input("Enter marks for Subject 1: "))
subject2_marks = float(input("Enter marks for Subject 2: "))
subject3_marks = float(input("Enter marks for Subject 3: "))

# Calculate average marks
obt_marks = (subject1_marks + subject2_marks + subject3_marks) 

persntage= (obt_marks/300)*100

# Determine grade based on average marks
if persntage >= 90:
    grade = "A"
elif persntage >= 80:
    grade = "B"
elif persntage >= 70:
    grade = "C"
elif persntage >= 60:
    grade = "D"
else:
    grade = "F"

# Print the grade
print("Your percentage are:", persntage)
print("Your grade is:", grade)


#------------------ Assigement no 3 part 2 -----------------#
x = int(input("enter your year to check leap year  "))

if (x % 400 == 0) or (x % 4 == 0 and x % 400 != 0):
    print("this is leaf year")
else:
    print("its not leap year")


#------------------ Assigement no 3 part 3 -----------------#
C = float(input("Enter value you want to change in  kelvin and fahrenheit"))

K = C + 273.15
F = (K - 273.15 ) * (5/9)+32

print("convert to kelvin", K)
print("convert to fahrenheit", F)

f = float(input("Enter temperature in fahrenheit to converts between celsius and kelvin"))

c = (f - (32)) * (5/9) 
K=(f-32) * (9/5)+273.15


print("convert to celsius", K)
print("convert to kelvin", F)

x = float(input("Enter temperature in kelvin to converts between celsius and fahrenheit"))

y= x-273.15
z = 26.85 * (9/5 )+32


print("convert to celsius", y)
print("convert to fahrenheit", z)




#---------------- Assigement no 3 part 4 ---------------#

p1 = int(input("enter first side of triangle "))
p2 = int(input("enter secound side of triangle "))
p3 = int(input("enter third side of triangle "))

if (p1==p2==p3):
    print("This is saclene triangle")
    
elif (p1==p2)or (p1==p3) or(p2==p3) or (p2==p1):
    print("This is isoscalene triangle")
    
elif (p1!=p2!=p3):
    print("This is Equiritral triangle")
else:("some thing was wrong")
