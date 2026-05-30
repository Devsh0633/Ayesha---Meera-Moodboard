import sys

replacements = {
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Bandhani_fabric_Rajasthan.jpg/800px-Bandhani_fabric_Rajasthan.jpg": "./photos/fabrics/bandhani.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Leheriya_saree.jpg/800px-Leheriya_saree.jpg": "./photos/fabrics/leheriya.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Gota_patti_embroidery_Rajasthan.jpg/800px-Gota_patti_embroidery_Rajasthan.jpg": "./photos/fabrics/gota_patti.jpg",
    
    "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/20111024_-_051_-_Royal_Gaitor.jpg/800px-20111024_-_051_-_Royal_Gaitor.jpg": "./photos/locations/gaitor_1.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/20111024_-_047_-_Royal_Gaitor.jpg/800px-20111024_-_047_-_Royal_Gaitor.jpg": "./photos/locations/gaitor_2.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/20111024_-_055_-_Royal_Gaitor.jpg/800px-20111024_-_055_-_Royal_Gaitor.jpg": "./photos/locations/gaitor_3.jpg",
    
    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Chandra_Mahal,_Jaipur,_Rajasthan_(India).jpg/800px-Chandra_Mahal,_Jaipur,_Rajasthan_(India).jpg": "./photos/locations/chandra_mahal.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Mubarak_Mahal_City_Palace.JPG/800px-Mubarak_Mahal_City_Palace.JPG": "./photos/locations/mubarak_mahal.jpg",
    
    "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Amer_Jaipur_-_Panna_Meena_ka_Kund_(2022)_-_img_08.jpg/800px-Amer_Jaipur_-_Panna_Meena_ka_Kund_(2022)_-_img_08.jpg": "./photos/locations/panna_meena_1.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Amer_Jaipur_-_Panna_Meena_ka_Kund_(2022)_-_img_04.jpg/800px-Amer_Jaipur_-_Panna_Meena_ka_Kund_(2022)_-_img_04.jpg": "./photos/locations/panna_meena_2.jpg",
    
    "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Sisodia_Rani_ka_Bagh_Jaipur.jpg/800px-Sisodia_Rani_ka_Bagh_Jaipur.jpg": "./photos/locations/sisodia_rani_1.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Sisodia_Rani_Palace_Jaipur.jpg/800px-Sisodia_Rani_Palace_Jaipur.jpg": "./photos/locations/sisodia_rani_2.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Sisodia_rani_garden.jpg/800px-Sisodia_rani_garden.jpg": "./photos/locations/sisodia_rani_3.jpg",
    
    "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Nahargarh_Biological_Park.jpg/800px-Nahargarh_Biological_Park.jpg": "./photos/locations/kishanbagh_1.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Aravalli_hills_Jaipur.jpg/800px-Aravalli_hills_Jaipur.jpg": "./photos/locations/kishanbagh_2.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Aravalli_Range_Rajasthan.jpg/800px-Aravalli_Range_Rajasthan.jpg": "./photos/locations/kishanbagh_3.jpg",
    
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/City_View_from_Nahargarh.jpg/800px-City_View_from_Nahargarh.jpg": "./photos/locations/nahargarh_1.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/City_beatutiful_and_fort_view_of_jaipur_NAHARGARH_(NARESH_KUMAR).jpg/800px-City_beatutiful_and_fort_view_of_jaipur_NAHARGARH_(NARESH_KUMAR).jpg": "./photos/locations/nahargarh_2.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Nahargarh_Fort_from_a_distance.jpg/800px-Nahargarh_Fort_from_a_distance.jpg": "./photos/locations/nahargarh_3.jpg",
    
    "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Amer_Fort_from_near_the_entrance.jpg/1280px-Amer_Fort_from_near_the_entrance.jpg": "./photos/locations/amber_fort_1.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Amber_Fort_Jaipur_2.jpg/1280px-Amber_Fort_Jaipur_2.jpg": "./photos/locations/amber_fort_2.jpg",
    
    "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Teej_festival_procession_Jaipur.jpg/800px-Teej_festival_procession_Jaipur.jpg": "./photos/festival/teej_procession_1.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Teej_procession_Rajasthan.jpg/800px-Teej_procession_Rajasthan.jpg": "./photos/festival/teej_procession_2.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Hariyali_Teej_Jaipur.jpg/800px-Hariyali_Teej_Jaipur.jpg": "./photos/festival/teej_procession_3.jpg",
    
    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Puja_Thali.jpg/800px-Puja_Thali.jpg": "./photos/festival/puja_thali.jpg",
    
    "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Rajasthani_jewellery.jpg/800px-Rajasthani_jewellery.jpg": "./photos/accessories/jewellery.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Lac_bangles_Jaipur.jpg/800px-Lac_bangles_Jaipur.jpg": "./photos/accessories/lac_bangles.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Rajasthani_jutti.jpg/800px-Rajasthani_jutti.jpg": "./photos/accessories/jutti.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Embroidered_potli_bag.jpg/800px-Embroidered_potli_bag.jpg": "./photos/accessories/potli_bag.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Gajra_India.jpg/800px-Gajra_India.jpg": "./photos/accessories/gajra_1.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Gajra_worn_by_woman.jpg/800px-Gajra_worn_by_woman.jpg": "./photos/accessories/gajra_2.jpg"
}

html_file = 'Ayesha -Meera Moodboard.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

for old, new in replacements.items():
    content = content.replace(old, new)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML file updated successfully.")
