# Create a set

set1={'pop','rock','soul','hard rock','rock','R&B','rock','disco'}
print(set1)

# Convert list to set

album_list={'Michael Jackson','Thriller',1982,'00:42:19',\
            'Pop, Rock, R&B',46.0,65,'30-Nov-82',None,10.0}
album_set=set(album_list)
print(album_set)

music_genres=set(['pop','rock','pop','folk rock','hard rock','soul',\
              'progressive rock','soft rock','R&B','disco'])
print(music_genres)

#Sampe set

A=set(['Thriller','Back in Black','AC/DC'])
print(A)

#Add element to set

A.add('NSYNC')
print(A)

#Try to add duplicate element to the set

A.add('NSYNC')
print(A)

#Remove the element from set

A.remove('NSYNC')
print(A)

#Verufy if the element is in the set

print('AC/DC' in A)
print('NSYNC' in A)

#Sample set

album_set_1=set(['Thriller','AC/DC','Back in Black'])
album_set_2=set(['AC/DC','Back in Black','The Dark Side of the Moon'])
print(album_set_1, album_set_2)

#Find the intersections

intersection=album_set_1&album_set_2
print(intersection)

inter=album_set_1.intersection(album_set_2)
print(inter)

# Find the difference in set1 but not set2

print(album_set_1.difference(album_set_2))

# Find the difference in set2 but not set1

print(album_set_2.difference(album_set_1))

#Find the union of two sets

print(album_set_1.union(album_set_2))

# Check if superset

print(album_set_1.issuperset(album_set_2))
print(album_set_1.issuperset({'AC/DC','Back in Black'}))
print(album_set_2.issuperset({'AC/DC','Back in Black'}))

#   Check if subset

print(album_set_1.issubset(album_set_2))
print(set(['Back in Black','AC/DC']).issubset(album_set_1))
print(set(['AC/DC','Back in Black']).issubset(album_set_2))

#Convert the list to a set

thelist=['rap','house','electronic music','rap']
theset=set(thelist)
print(theset)

print(set(['rap','house','electronic music','rap']))


A=[1,2,2,1]
B=set([1,2,2,1])
print('The sum of A is: ',sum(A))
print('The sum of B is: ',sum(B))

album_set_3=album_set_1.union(album_set_2)
print(album_set_3)

print(album_set_1.issubset(album_set_3))
