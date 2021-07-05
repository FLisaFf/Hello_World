#create a list

L=['Michael Jackson',10.1,1982]
print(L)

#print the elements on each index

print('the same element using negative and positive indexing: \n Positive:',L[0],
      '\n Negative:' , L[-3] )
print('the same element using negative and positive indexing: \ Positive:' ,L[1],
      '\n Negative:' , L[-2])
print('the same element using negative and positive indexing: \n' , L[2],
      '\n Negative:' , L[-1])

#sample list

list1=['Michael Jackson', 10.1, 1982, [1, 2], ('A', 1)]
print(list1[3:5])

#use extend to add elements to list
list1.extend(['pop', 10])
print(list1)

#use append to add elements to the list

list1.append(['hello', 10.1, 1])
print(list1)

#change the element based on the index

A=['disco', 10, 1.2]
print('Before change:',A)
A[0]='hard rock'
print('After change:',A)

#delete the element based on index

print('Before change:', A)
del(A[0])
print('After change:', A)

#split the string, default is by space

print('hard rock'.split())

#split the string by comma

print('A,B,C,D'.split(','))

#copy (copy by reference) the list A

A=['hard rock', 12, 1.2]
B=A
print('A:', A)
print('B:', B)

#examine the copy by reference

print('B[0]:',B[0])
A[0]='banana'
print('B[0]:',B[0])

#clone the list A
B=A[:]
print(B)

print('B[0]:', B[0])
A[0]='POP'
print('B[0]:',B[0])

#MY OWN LIST

a_list=[1,'hello',[1,2,3],True]
print(a_list)

print(a_list[1])

print(a_list[1:4])

A=[1,'a']
B=[2,1,'d']
C=A+B
print(C)




