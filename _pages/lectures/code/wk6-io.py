from pathlib import Path

home_dir = "/home/acacia"
home_path = Path(home_dir)
doc_path = home_path / "Documents"
pic_path = home_path / "Pictures"
python_path = doc_path / "CMSC-140-WT-23"

print(home_dir)
print(home_path)
print(doc_path)
print(python_path)


hello = open("data/hello.txt")
print(hello)
#file_contents = hello.read()
#print(file_contents)
file_contents_list = hello.readlines()
print(file_contents_list)
for i in file_contents_list:
    print(i)
# Absolute: /home/acacia/Documents/CMSC-140-WT-23/_pages/lectures/code/hello.txt

writer_file = open('writing.txt', 'w')
writer_file.write("new content")
writer_file.close()

writer_file = open('writing.txt', 'a+')
writer_file.write("\nmore new content")
filelines = writer_file.read()
writer_file.close()

with open('writing.txt') as f:
    file_content = f.readlines()

print(file_content)

temps = []
hats = [] 
with open("temps.txt") as f:
    next(f)
    for line in f.readlines():
        t, h = line.split(" ")
        # thisline = line.split(" ")
        # t = thisline[0]
        # h = thisline[1]
        temps.append(int(t))
        hats.append(int(h))
print(temps)
print(hats)
