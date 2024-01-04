# Program to find the missing numbers in an array

def findmissingnumbers(n):
    numbers = set(n)
    print(numbers)
    output = []
    for i in range(1,n[-1]):
        if i not in numbers:
            output.append(i)
    return output

number_list= [1,2,3,5,6,8,9,13]
print(findmissingnumbers(number_list))
print('done')

