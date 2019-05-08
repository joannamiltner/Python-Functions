# # Print all integers from 0 to 150
for x in range (151):
    print(x)

# # Print all the multiples of 5 from 5 to 1000
for v in range (5, 1001, 5):
    print (v)

# # Print integers 1 to 100. if divisable by 5, print "Coding" instead. If divisable by 10, print "Coding Dojo"
def countingDojo():   
    for v in range (1, 101):
        if v % 10==0:
            print ("Coding Dojo")
        elif v % 5==0:
            print ("Coding")
        else: 
            print(v)
countingDojo()

# # Add odd integers from 0 to 500,000, and print the final sum
def finalsum():
    sum=0
    for i in range (1, 500001, 2):
        sum+=i
    print (sum)
finalsum()

# # Print positive numbers starting at 2018, counting down by fours
def twoe():
    for v in range (2018, 0, -4):
        print (v)
twoe()

# Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers taht are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3,6,9 (on sucessive lines)
for num in range (2, 10):
    if num%3==0:
        print (num,"\n")
