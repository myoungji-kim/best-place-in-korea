import crawling
import folium
from geopy.geocoders import Nominatim

def drawing_map(url):
    sites = crawling.crawling_sites(url)[0]
    map = folium.Map(location=[36.501, 127.870], zoom_start=7)
    geolocator = Nominatim(user_agent='main')

    for site in sites:
        # print(site)
        if site == 'Canadian High Arctic':  # 74.75, 265.00
            site_loc = [74.75, 265.00]
        else:
            site_geodata = geolocator.geocode(site)
            site_loc = [site_geodata.latitude, site_geodata.longitude]
        folium.Marker(location=site_loc, popup=site).add_to(map)
    return map
    