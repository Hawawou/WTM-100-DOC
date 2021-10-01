# open the file in read only mode
file = open('Day20/file.txt', 'r')
type(file)

# raw file types are opened as
open('Day20/file.txt', 'rb', buffering=0)
