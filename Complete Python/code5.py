# Data Type
# List : Collection of diff items (data type)
marks=[10,74,85,96,95,'A','97.3']
print(marks,type(marks))
# Operations of list
#length
print(len(marks))
#index
print(marks[5])
print(marks[-1]) # Last Index
# Slicing a list : list[start:end]
print(marks[0:3])
print(marks[-3:])
for score in marks:
    print(score)

# it is Mutable : 'We can change Here
marks.append(50)
print(marks)
# marks.insert(0,50) ---> (index,added value)
#print(marks)
# Check Existance value find
print(97 in marks)


# Tuple - Imutable : We can't Change its value
rollnum=(20,48,78,86,59,95,86)
print(rollnum,type(rollnum))

# Operations
#index value
print(rollnum[3])
# cont num of time
print(rollnum.count(86))
print(rollnum.index(86))

# Set: Collection of uniqe items
snum={47,85,85,95,86,95}
print(len(snum),snum) # 4
for i in snum:
    print(i)


# Dictionary : Collection of key Value pairs :it is Mutable
student_marks={"math":97,"phy":85,"che":97}
print(student_marks,type(student_marks))
student_marks["phy"]=88
print(student_marks["phy"])
# add also
student_marks["Eng"]=78
print(student_marks)

for key in student_marks:
    print(key,student_marks[key])

    # mutable data type is slower as compare to imutable data type

    #Tupple is faster as compare to list



