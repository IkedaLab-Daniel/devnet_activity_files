myList = ["Apple", "Pineapple", "waterapple", "Bananapple"]

print(f"""
    |-------------------------- Old List --------------------------|
      {myList}
    |--------------------------------------------------------------|

      """)

myList.append("Orapple")

print(f"""
    |-------------------------- New List --------------------------|
      {myList}
    |--------------------------------------------------------------|

      """)

print(myList[-2])

x = 0

while x < len(myList):
    print(f"{x+1}. {myList[x]}")
    x = x + 1

myList.insert(2, "Melonapple")

print(f"""
    |-------------------------- New List --------------------------|
      {myList}
    |--------------------------------------------------------------|

      """)

myList[0] = "NEW VALUE"

print(f"""
    |-------------------------------------- New List --------------------------------------|
      {myList}
    |--------------------------------------------------------------------------------------|

      """)

print(myList)

myList.remove("NEW VALUE")

print(myList)

name = "Mark \nDaniel \nCallejas"
print(name[0:1])

myList.remove("Bananapple")
print(myList)

myList[0:2] = ["Apple", "Bananapple  ", "Siresa"]
print(myList)

myList.pop(0)
print(myList)

for fruit in myList:
    print(fruit)

print(len(myList))