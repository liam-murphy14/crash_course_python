with open("responses.txt", 'a') as file_obj:
    while True:
        inp = input("why do you love python ?? (type q to quit)\n")
        if inp == 'q':
            exit()
        inp = inp + '\n'
        file_obj.write(inp)