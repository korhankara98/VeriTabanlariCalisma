from astroquery.simbad import Simbad
import pandas as pd

Simbad.add_votable_fields('distance', 'ra', 'dec')

pn = ['NGC 7293', 'NGC 6826', 'NGC 6543', 'NGC 7009', 'NGC 3132', 'NGC 6720']

results = []
for nebula in pn:
    result = Simbad.query_object(nebula)
    if result:
        distance = result['Distance_distance'][0]
        ra = result['RA'][0]
        dec = result['DEC'][0]
        results.append({'Name': nebula, 'RA': ra, 'DEC': dec, 'Distance (pc)': distance})

df = pd.DataFrame(results)
print(df)
