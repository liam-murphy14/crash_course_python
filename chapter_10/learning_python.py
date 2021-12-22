with open("learning.txt") as file_object:
    lines = file_object.readlines()
for line in lines:
    line = line.replace("python", "java")
    line = line.replace("Java", "ocaml")
    line = line.replace("Ocaml", "python")
    line = line.strip().lower()
    print(line)
