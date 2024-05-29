# Iterate over dictionary Keys
print("Iterate over dictionary Keys \n")
chemical_elements = {
    "Hydrogen":"H",
    "Helium":"He",
    "Beryllium":"B",
    "Boron":"B",
    "Carbon":"C",
    "Nitrogen":"N",
    "Oxygen":"O",
    "Flourine":"F",
    "Neon":"Ne"
}

### Method 1 ###
print("Method 1")
print(list(chemical_elements.keys()))

print("")
### Method 2 ###
print("Method 2")
for element in chemical_elements.keys():
    print(element, end=" ")




