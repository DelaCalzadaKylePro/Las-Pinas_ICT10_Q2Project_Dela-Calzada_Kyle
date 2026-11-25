from pyscript import document

non_metals = {
    "H": ("Hydrogen", 1, "1.008"),
    "C": ("Carbon", 6, "12.011"),
    "N": ("Nitrogen", 7, "14.007"),
    "O": ("Oxygen", 8, "15.999"),
    "P": ("Phosphorus", 15, "30.974"),
    "S": ("Sulfur", 16, "32.06"),
    "Se": ("Selenium", 34, "78.971"),
    "F": ("Fluorine", 9, "18.998"),
    "Cl": ("Chlorine", 17, "35.45"),
    "Br": ("Bromine", 35, "79.904"),
    "I": ("Iodine", 53, "126.904"),
    "At": ("Astatine", 85, "[210]"),
    "Ts": ("Tennessine", 117, "[294]"),
    "He": ("Helium", 2, "4.0026"),
    "Ne": ("Neon", 10, "20.180"),
    "Ar": ("Argon", 18, "39.948"),
    "Kr": ("Krypton", 36, "83.798"),
    "Xe": ("Xenon", 54, "131.293"),
    "Rn": ("Radon", 86, "[222]"),
    "Og": ("Oganesson", 118, "[294]"),
}

def find_element(e):
    document.getElementById("result").innerHTML = ""
    symbol = document.getElementById("elementInput").value.strip().capitalize()
    element_data = non_metals.get(symbol)
    element_name, atomic_number, atomic_mass = element_data if element_data else (None, None, None)
    document.getElementById("result").innerHTML = (
        f"<b>Symbol:</b> {symbol}<br>"
        f"<b>Element Name:</b> {element_name}<br>"
        f"<b>Atomic Number:</b> {atomic_number}<br>"
        f"<b>Atomic Mass:</b> {atomic_mass}<br>"
        if element_data
        else "Element symbol not found in the list of non-metals."
    )
