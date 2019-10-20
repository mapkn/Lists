# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 13:00:55 2018

@author: patemi
"""
import numpy as np
from functools import reduce 

###################CREATING LISTS

# declare an empty list
list77=[]


# Create a list with 5 selements, all 0
list0=[0]*5

list1=[3600.0,5400.0,500,6600]
list2=[5,6,7,8]
#############################################


# Position of an element in a list
print(["foo", "bar", "baz"].index("bar"))



# Take absolute of value-8, using list comprehension
anotherlist=[abs(value-8) for value in list2]


# Smallest element of list1 greater than 3700
list50=[x for x in list1 if x > 6700]
if not list50:
    list50=list1[-1]
else:
    list50=min([x for x in list1 if x > 6700])


# Largest element of list1 smaller than 3700
list60=[x for x in list1 if x < 6700]
if not list60:
    list60=list1[0]
else:
    list60=max([x for x in list1 if x < 6700])



# Element wise difference between list elements
print(list(set(list1)-set(list2)))


# last and first elements
print(list2[-1])
print(list2[0])


# using range and arange to create the lists 
times=list(range(0,10));
times2=list(np.arange(0,10,0.25));

##########################################

############Zip lists##################

# initializing lists 
name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ] 
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 40, 50, 60, 70 ] 
  
# using zip() to map values 
mapped = zip(name, roll_no, marks) 
  


# converting values to print as set 
mapped = set(mapped) 


# Zip + comprehension

l1 = [100,200,300]
l2 = [0,1,2]

#l3=zip(l1,l2)

p=[x + y for x,y in zip(l1,l2)]

###############################################

############## LIST ENUMERATION ################

# looping if we don't need the indexes
for item in list1:
    print(item)

# Looping through in reverse order
for item in list1[::-1]:
    print(item)

# Looping using enumerate
#for i,v in enumerate(list1):
#    print(i)
    

# Enumerating two lists simultaneously
#https://stackoverflow.com/questions/16326853/enumerate-two-python-lists-simultaneously

data1=[5,4,3]
data2=[4,1,2]

data3=[6,7,8,9,10,11]

for index, (value1, value2) in enumerate(zip(data1, data2)):
    print(index, value1 + value2)



###############################################



# Take max and min of list elements
ma=max(list1)
mi=min(list1)


# Add one to each list element
list2=[x+1 for x in list1]

# List comprehension: return only the positive values
list3=[x for x in list1 if x>0]

y=np.array([x for x in list1 if x==5500])

# Return the indices which meet the specified criteria
indices=[i for i,v in enumerate(list1) if v-5000>0]
         
# Return the values for the specified index
values=[v for i,v in enumerate(list1) if i==1]
        
# How to check if a list is empty        
list5=[]
#print(if list5)

if list5:
    print('Not Empty')
else:
    print('Empty')
    

# Reduce list of lists to list
# Reduce will produce a unique list 
# Note: duplicate entries will be removed. 
#l = [[1,2,3],[4,5,6], [7], [8,9]]
#l = [2,[2,3]]
#l = [[2],[2,3]]
#



l = [[2],[2]]
# if integers in list, then just get addition
#l = [2,2]
ll=reduce(lambda x,y: x+y,l)


# For an empty list need to use initialiser [] when using "reduce"
l1 = []
l1=reduce(lambda x,y: x+y,l1,[])


l2 = [[5.0]]
l2=reduce(lambda x,y: x+y,l2)


####################################
# Converting List of list to array

listoflist=[[3,4,5],[5,6,7]]
arraylistoflist=np.array(listoflist)

print(listoflist)
print(arraylistoflist)
print(arraylistoflist[:,0])

###################################

# Converting a list to numpy array and then use numpy functions where to filter
tup=np.where(np.array(list1)<5000)


# append an item to a list
mylist=[]
mylist.append('T')
mylist.append(l)


# Check if all elements in a list are the same
#print(len(set(mylist)))
z=all(x == mylist[0] for x in mylist)





# Function to convert list elements to float
def convertlistofliststofloat(_list):
    output_list=[]
    for l in _list:
        l=[float(i) for i in l]
        output_list.append(l)
    return output_list


# Function to convert list elements to float
def convertlistelementstofloat(l):
    return [float(i) for i in l]



# Function to convert list elements to float
# Nested list comprehensions
def convertlistoflistelementstofloat(non_flat):
    #for item in non_flat:
    #    for y in item:
    #        float(y)
    
    return [float(y) for item in non_flat for y in item]
    # https://spapas.github.io/2016/04/27/python-nested-list-comprehensions/


# Creating a list of Objects

class factor():
    def __init__(self, category, risk_class):
        self.category = category
        self.risk_class = risk_class


factorlist=[factor('BOR','GIRR'),factor('OIS','GIRR')]

f1=factorlist[0]
print(f1.category)

### Delete items using index

del(list0[0])



###################################################
############# Sorting Lists


# Sort in place
list3.sort()


# Return to new variable
listx=sorted(list1)

#l2[]



def outside_list_range(mylist,val):
    #returns true if val is not within the range of values in mylist
    if above_list_maximum(mylist,val):
        return True
    elif below_list_minimum(mylist,val):
        return True
    else:
        return False
    
                
    
def above_list_maximum(mylist,val):
    #returns true if val is not within the range of values in mylist
    maxlist=max(mylist)
    if val>maxlist:
        return True
    else:
        return False
    

def below_list_minimum(mylist,val):
    #returns true if val is not within the range of values in mylist
    minlist=min(mylist)
    if val<minlist:
        return True
    else:
        return False
