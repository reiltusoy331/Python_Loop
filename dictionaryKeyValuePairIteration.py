print("Iterate over dictionary Key Value Pairs \n")
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

print(" ")

### Method 1 ###
print("Method 1")
print(list(chemical_elements.items()))

print("")

print("Method 2")
for element, symbol in chemical_elements.items():
    print(element,symbol)


