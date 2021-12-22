while True:
    num_string = input("enter numbers to add, or q to quit\n")
    if num_string == 'q':
        exit()
    nums = num_string.split()
    final = 0
    for num in nums:
        try:
            n = int(num)
        except ValueError:
            pass
        else:
            final += n
    print(final)
    