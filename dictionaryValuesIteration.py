# Iterate over dictionary Values

print("Iterate over dictionary Values \n")
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
print(list(chemical_elements.values()))

print("")

print("Method 2")
for chem_symbol in chemical_elements.values():
    print(chem_symbol,end=' ')


