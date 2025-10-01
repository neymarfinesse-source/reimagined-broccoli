import random

# List of metals with their common oxidation states
metals = [
    {"symbol": "Co", "name": "cobalt", "oxidation": [2, 3]},
    {"symbol": "Cu", "name": "copper", "oxidation": [1, 2]},
    {"symbol": "Fe", "name": "iron", "oxidation": [2, 3]},
    {"symbol": "Cr", "name": "chromium", "oxidation": [2, 3]},
    {"symbol": "Pt", "name": "platinum", "oxidation": [2, 4]},
]

# Ligand data: (formula, IUPAC name for ligand, charge)
ligands = [
    ("NH3", "ammine", 0),
    ("H2O", "aqua", 0),
    ("Cl", "chloro", -1),
    ("NO2", "nitrito-N", -1),
    ("en", "ethylenediamine", 0),
    ("CN", "cyano", -1),
    ("OH", "hydroxo", -1),
]

# Function to randomly choose ligands
def choose_ligands():
    n_ligands = random.randint(2, 4)
    chosen = random.sample(ligands, n_ligands)
    counts = [random.randint(1, 4) for _ in chosen]
    return list(zip(chosen, counts))

# Generate random complex
metal = random.choice(metals)
oxidation = random.choice(metal["oxidation"])
chosen_ligands = choose_ligands()

# Compute overall charge
charge = oxidation
for ((formula, name, ligand_charge), count) in chosen_ligands:
    charge += ligand_charge * count

# Sorting ligands alphabetically by their name for naming
sorted_ligands = sorted(chosen_ligands, key=lambda x: x[0][1])

# Building the formula and name
formula_parts = []
name_parts = []

prefixes = {1: '', 2: 'di', 3: 'tri', 4: 'tetra'}

for ((formula, name, ligand_charge), count) in sorted_ligands:
    formula_parts.append(f"{formula}{count if count > 1 else ''}")
    # For polydentate ligand with prefix in name (like ethylenediamine), use 'bis', 'tris'
    if name == "ethylenediamine":
        ligand_prefix = {1: "", 2: "bis", 3: "tris", 4: "tetrakis"}[count]
        name_parts.append(f"{ligand_prefix}({name})")
    else:
        name_parts.append(f"{prefixes[count]}{name}")

formula_str = f"[{metal['symbol']}{''.join(formula_parts)}]"
if charge != 0:
    formula_str += f"{'^' + str(charge) if charge > 0 else '^' + str(charge)}"

name_str = f"{''.join(name_parts)}{metal['name']}({oxidation})"

print(f"Coordination Compound Formula: {formula_str}")
print(f"Systematic Name: {name_str} ion")
