# Write a Python function graphSnowfall(t) which retrives data in a text file t and displays that information in a bar chart.

# function grahSnowFall()
def graphSnowFall(t):

    counter = [0, 0, 0, 0, 0]

    file = open("t.txt", "r")
    for line in file:
        snow = int(line.strip())
        if snow < 11:
            counter[0] += 1
        elif snow < 21:
            counter[1] += 1
        elif snow < 31:
            counter[2] += 1
        elif snow < 41:
            counter[3] += 1
        else:
            counter[4] += 1
    file.close()

    print(counter[0], "between 0-10cms")
    print(counter[1], "between 0-10cms")
    print(counter[2], "between 0-10cms")
    print(counter[3], "between 0-10cms")
    print(counter[4], "between 0-10cms")


graphSnowFall("t.txt")