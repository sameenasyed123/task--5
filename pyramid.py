#To create pyramid of numbers from 1 t0 20 using for loop.

#How many rows we want in pyramid
#declare that rows assign to the rows

rows = 21
#by using for loop from where to stop the pyramid of count.
for i in range(1, rows):
    #it will increment line byline by adding the i value with 1
    for j in range(1, i + 1):
        
        print(j, end=' ')
    print("")
