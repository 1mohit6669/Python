n= input('value of n: ')
Students = {}# create a empty dictionary to store student names and their marks

for i in range(int(n)):
    # Input line containing name and mark
    line =input('line value:').split()
    name =line[0]
    marks =list(map(float,line[1:]))# convert marks to float
    # Store name and marks in the dictionary
    Students[name] = marks

# Name to query
query = input('valu of query: ')

# Calculate and print average
avg = sum(Students[query]) / len(Students[query])# calculate average of marks
# Print the average rounded to two decimal places
print(f"{avg:.2f}")
