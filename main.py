from pyscript import document,display

# Dictionary information about planets
# Element Symbol : Element name, atomic #, atomic mass

element = {
"H": ("Hydrogen", 1, 1.008),
"HE": ("Helium", 2, 4.0026),
"C": ("Carbon", 6, 12.011),
"N": ("Nitrogen", 7, 14.007),
"O": ("Oxygen", 8, 15.999),
"F": ("Fluorine", 9, 18.998),
"FE": ("Neon", 10, 20.180),
"P": ("Phosphorus", 15, 30.974),
"S": ("Sulfur", 16, 32.06),
"CL": ("Chlorine", 17, 35.45),
"AR": ("Argon", 18, 39.948),
"SE": ("Selenium", 34, 78.971),
"BR": ("Bromine", 35, 79.904),
"KR": ("Krypton", 36, 83.798),
"I": ("Iodine", 53, 126.90),
"XE": ("Xenon", 54, 131.29),
"AT": ("Astatine", 85, 210),
"RN": ("Radon", 86, 222),
"TS": ("Tennessine", 117, 294),
"OG": ("Oganesson", 118, 294)

 }

# function to search planet
def search_element(e):
    # Get the input from HTML

    Element1 = document.getElementById("element1").value.upper()
    # retrieve information from the dictionary
    result = element.get(Element1, ('Element not found', "-", "-"))

    document.getElementById("symbol").innerText = Element1
    document.getElementById("name").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]

