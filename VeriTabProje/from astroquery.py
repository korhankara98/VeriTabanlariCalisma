from astroquery.simbad import Simbad
from astroquery.gaia import Gaia

custom_simbad = Simbad()
custom_simbad.add_votable_fields('distance')

result = custom_simbad.query_object("NGC  6439")

if result:
    distance = result['Distance_distance'][0]
    print(f"NGC  6439 Uzaklığı: {distance} parsek")

    distance_min = distance - 10
    distance_max = distance + 10

    job = Gaia.launch_job(f"""
        SELECT 
            source_id, 
            ra, 
            dec, 
            parallax, 
            parallax_error 
        FROM 
            gaiadr2.gaia_source 
        WHERE 
            parallax BETWEEN {1000/distance_max} AND {1000/distance_min}
        """)
    
    gaia_results = job.get_results()

    if not gaia_results:
        print("Aynı bölgede ve aynı uzaklıkta olan cisimler bulunamadı.")
    else:
        for row in gaia_results:
            print(f"ID: {row['source_id']}, RA: {row['ra']}, DEC: {row['dec']}, Paralaks: {row['parallax']}, Paralaks Hatası: {row['parallax_error']}")
else:
    print("NGC  6439 için bilgi bulunamadı.")
