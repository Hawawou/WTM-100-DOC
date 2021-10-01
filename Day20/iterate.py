# iterating over each line
with open('Day20/file.txt', 'r') as reader:
    # read and print the entire file line by line
    line = reader.readline()
    while line != '':
        print(line, end='') 
        line = reader.readline()
    
    
# alternatively
with open('Day20/file.txt', 'r') as reader:
    for line in reader.readlines():
        print(line, end='') 
        
        
# also
with open('Day20/file.txt', 'r') as reader:
    for line in reader:
        print(line, end='')
        