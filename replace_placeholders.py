import sys

replacements = {
    "PLACEHOLDER_BANDHANI_FABRIC_CLOSEUP": "./photos/fabrics/bandhani_closeup.jpg",
    "PLACEHOLDER_LEHERIYA_FABRIC_CLOSEUP": "./photos/fabrics/leheriya_closeup.jpg",
    "PLACEHOLDER_GOTA_FABRIC_CLOSEUP": "./photos/fabrics/gota_closeup.jpg",
    
    "PLACEHOLDER_GAITORE_SHOOT_1": "./photos/locations/gaitore_columns.jpg",
    "PLACEHOLDER_GAITORE_SHOOT_2": "./photos/locations/gaitore_group.jpg",
    "PLACEHOLDER_CITY_PALACE_SHOOT_1": "./photos/locations/city_palace_shoot.jpg",
    "PLACEHOLDER_CITY_PALACE_SHOOT_2": "./photos/locations/city_palace_group.jpg",
    "PLACEHOLDER_PANNA_MEENA_SHOOT_1": "./photos/locations/panna_meena_shoot.jpg",
    "PLACEHOLDER_PANNA_MEENA_SHOOT_2": "./photos/locations/panna_meena_group.jpg",
    "PLACEHOLDER_SISODIA_BAGH_SHOOT_1": "./photos/locations/sisodia_swing.jpg",
    "PLACEHOLDER_SISODIA_BAGH_SHOOT_2": "./photos/locations/sisodia_group.jpg",
    "PLACEHOLDER_AMBER_FORT_SHOOT_1": "./photos/locations/amber_fort_shoot.jpg",
    "PLACEHOLDER_AMBER_FORT_SHOOT_2": "./photos/locations/amber_fort_group.jpg",
    
    "PLACEHOLDER_CAFE_LOCATION": "./photos/everyday/cafe_location.jpg",
    "PLACEHOLDER_CAFE_SHOOT": "./photos/everyday/cafe_shoot.jpg",
    "PLACEHOLDER_OFFICE_LOCATION": "./photos/everyday/office_location.jpg",
    "PLACEHOLDER_OFFICE_SHOOT": "./photos/everyday/office_shoot.jpg",
    "PLACEHOLDER_HOME_COURTYARD": "./photos/everyday/home_courtyard.jpg",
    "PLACEHOLDER_HOME_SHOOT_1": "./photos/everyday/home_shoot_1.jpg",
    "PLACEHOLDER_HOME_SHOOT_2": "./photos/everyday/home_shoot_2.jpg",
    "PLACEHOLDER_STREET_LOCATION": "./photos/everyday/street_location.jpg",
    "PLACEHOLDER_STREET_SHOOT": "./photos/everyday/street_shoot.jpg",
    "PLACEHOLDER_ROOFTOP_LOCATION": "./photos/everyday/rooftop_location.jpg",
    "PLACEHOLDER_ROOFTOP_SHOOT": "./photos/everyday/rooftop_shoot.jpg"
}

html_file = 'Ayesha -Meera Moodboard.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

for old, new in replacements.items():
    content = content.replace(old, new)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML file updated with placeholder paths.")
