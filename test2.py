# this is list code
list2=[22,33.5,32,"ANSARI"]
list2.append(99)
list2.insert(0,"Abdul")
list2.remove(33.5)
list2.pop(0)
print(list2.index("ANSARI"))
#list2.clear()
print(list2)

#this is set code
set={15,25,"dilsad"}
set.add("siddhi")
set.remove("dilsad")
set.clear()
print(set)

# this is disc.. code
disc1={(12):["dilsad"],(13):["Akash"],(14):["Abdul"]}
disc2={(15):["Saniya"],(16):["Abhimanyu"],(17):["Shivani"]}
disc2.update(disc1)
print(disc2)
print(disc2.keys())
print(disc2.values())
print(disc2.items())
print(disc2.get(17))
disc1.clear()
print(disc1)
