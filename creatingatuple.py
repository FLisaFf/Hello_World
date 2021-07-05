#create your ferst tuple

tuple1=('disco',10,1.2)
print(tuple1)

#print the type of a tuple I created

print(type(tuple1))

#print the variable on each index

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

#print hte type of value on each index

print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

#use negative index to get the value of the last element

print(tuple1[-1])

#use negative index to get the value of the second last element

print(tuple1[-2])

#use negative index to get the value of the third last element

print(tuple1[-3])

#concetenate 2 tuples

tuple2=tuple1+('hard rock', 10)
print(tuple2)

#slicing

print(tuple2[0:3])
print(tuple2[3:5])

#slice from index 0 to index 2

print(tuple2[0:3])

#slice from index 3 to index 4

print(tuple2[3:5])

#get the lenght of a tuple

print(len(tuple2))

#sorting
#a sample tuple

Ratings=(0,9,6,5,10,8,9,6,2)
Ratings1=sorted(Ratings)
print(Ratings1)

#create a nest tuple

NestedT=(1,2,('pop','rock'),(3,4),('disco',(1,2)))

#print element on each index

print('Element 0 of Tuple: ', NestedT[0])
print('Element 1 of Tuple: ', NestedT[1])
print('Element 2 of Tuple: ', NestedT[2])
print('Element 3 of Tuple: ', NestedT[3])
print('Element 4 of Tuple: ', NestedT[4])

#print element on each index, including nest indexing

print('Element 2, 0 of Tuple: ', NestedT[2][0])
print('Element 2, 1 of Tuple: ', NestedT[2][1])
print('Element 3, 0 of Tuple: ', NestedT[3][0])
print('Element 3, 1 of Tuple: ', NestedT[3][1])
print('Element 4, 0 of Tuple: ', NestedT[4][0])
print('Element 4, 1 of Tuple: ', NestedT[4][1])

#print the first element in the second nested tuples

print(NestedT[2][1][0])

#print the second element in the second nested tuples

print(NestedT[2][1][1])

#print the first element in the second nested tuples

print(NestedT[4][1][0])

#print the second element in the second nested tuples

print(NestedT[4][1][1])




#sample tuple

genres_tuple=('pop','rock','soul','hard rock','soft rock', \
              'R&B', 'progressive rock', 'disco')
print(genres_tuple)
print('The lenght of the Tuple: ',len(genres_tuple))
print(genres_tuple[3])
print(genres_tuple[3:6])
print(genres_tuple[0:2])
print(genres_tuple[-1][0])
print(genres_tuple.index('disco'))






