#Elise Ward and Abby Newton

def total_length(list):
    total = 0
    for x in list:
        total += len(x)
    return total
print(total_length(['Queen','rules']))
print(total_length([]))
print(total_length(['balloons']))
print(total_length(["",'',"",'']))


