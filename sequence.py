n = int(input("Enter the length of the sequence: ")) # Do not change this line

# insert number n 
# assign x = 0
# while loop for x < n
# define a b c to 0 1 0
# create trib variable that is sum of a b c
# assign a,b,c to trib, b, c
# increment x by 1
# print each number successively

x = 0 

a = 0
b = 1
c = 0
while x < n:
    

    trib = a + b + c

    a, b, c, = trib, a, b

    x += 1
    

    print(trib)
