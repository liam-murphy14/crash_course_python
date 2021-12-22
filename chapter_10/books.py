def count_words(file):
    try:
        with open(file) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(len(contents))
count_words(input("type filename: "))