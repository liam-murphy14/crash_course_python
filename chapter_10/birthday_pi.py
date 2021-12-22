with open("pi.txt") as file_object:
    contents = file_object.read().strip()
birthday = input("mmddyy: ")
if birthday in contents:
    print("your bday is in the first million digits of pi !!")
    