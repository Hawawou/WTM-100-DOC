d_path = 'Day20/file2.txt'
d_r_path = 'Day20/file.txt'
with open(d_path, 'r') as reader, open('Day20/file.py', 'a') as writer:
    file = reader.readlines()
    writer.writelines(file)