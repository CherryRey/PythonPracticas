list1 = [54, 44, 27, 79, 91, 41]

#def removeindex():
print(list1)
item = list1.pop(4)
print(f"The 4 index is out {list1}\n {item}")
list1.insert(2, item)
print(f"and now is in the 2 index {list1} \n {item}")
list1.append(item)
print(f"and now is also in the last position too {list1}\n{item}")

