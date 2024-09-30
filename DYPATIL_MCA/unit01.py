print("Hello !!!")

# i = Imaginary Number 

c = (3 + 6j)

print(c)

complexNum = complex(5,2)

print(complexNum)

# list Is sequence DataType , list store any Type Datatype Hetro , list is muteble

listDataType = [10,20,30,40,'LIST']  
print(listDataType)
print(type(listDataType))

print(listDataType[1: :2]) 

listSlice = [10,20,30,40,'MCA',[1,2,5]]  
print(listSlice[5][1])   

listSlice[5][1] = 4
print(listSlice[5][1])   
print(listDataType[ : : -2])   

listDataType.insert(2,"MBA")
print(listDataType)

listDataType.append("Pass")
print(listDataType)

# if want to join 2 list use Extend  [10,20,30,40,'LIST']  

extendList = listDataType.extend(listSlice)
print("extend Function",listDataType)


listDataType.append(listSlice)
print("append",listDataType)

listDataType.reverse()
print("reverse ",listDataType)

# +++++ SORT LIST+++++++++++++++++++

sortList = [10,50,20,60,70,4]
sortList.sort()
print(sortList)