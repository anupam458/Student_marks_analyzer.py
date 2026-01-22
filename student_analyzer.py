marks = []

n = int(input("Enter number of students = "))

for i in range(n):
    m = int(input("Enter mark = "))
    marks.append(m)

print(marks)
def average(marks):
    total = 0
    count = 0
    for m in marks:
        total = total + m 
        count += 1
    return total/ count
print("Average is = ",average(marks))

def highest( marks ):
    high = marks [ 0 ]
    for m in marks :
        if m > high:
            high = m 
    return high
print("The highest is = ",highest(marks))

def lowest( marks ):
    low = marks[ 0 ]
    for m in marks:
        if m < low :
            low = m
    return low
print("The lowest is = ",lowest(marks))

def pass_fail(marks):
    fail = 0
    for m in marks:
        if m < 40:
            fail += 1
    return fail
print("No of students failed = ",pass_fail(marks))
       
