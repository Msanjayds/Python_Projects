# Manually compute the Program Execution time
from time import time
start = time()

# program to create Acronyms
word = 'Artifical Intelligence'
text = word.split()
a = ''
for i in text:
    a = a+i[0]
print(a)
end = time()

Exectution_time = end - start
print('Exectution Time :', Exectution_time)