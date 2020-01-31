import time
from binary_search_tree import BinarySearchTree

#original runtime:0(n^c)
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

#create two binary tree objects
binary_tree1 = BinarySearchTree("names1")
binary_tree2 = BinarySearchTree("names2")

#add the names from the first list to the first binary tree
for i in range(0, len(names_1)):
    binary_tree1.insert(names_1[i])

#add the names from the second list to the second binary tree
for i in range(0, len(names_2)):
    binary_tree2.insert(names_2[i])

#check if the names in the first binary tree are duplicated in the second binary tree
for i in range(0, len(names_1)):
    if binary_tree2.contains(names_1[i]):
        duplicates.append(names_1[i])

"""for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)"""

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
