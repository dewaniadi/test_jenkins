import requests
import json
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def get_astronauts():

    r = requests.get(url='http://api.open-notify.org/astros.json')
    data = json.loads(r.content)
    names = []
    for each in data['people']:
        names.append(each['name'])
    return names

def get_position():

    r = requests.get(url='http://api.open-notify.org/iss-now.json')
    data = json.loads(r.content)

    return float(data['iss_position']['latitude']),\
        float(data['iss_position']['longitude'])

def map_iss_position(lat, lon):

    m = Basemap(projection='hammer',lon_0=0, lat_0=0)
    m.drawcoastlines()
    m.drawmapboundary(fill_color='aqua')
    m.fillcontinents(color='coral', lake_color='aqua')
    x, y = m(lon, lat)
    m.plot(x, y, color='m', marker='D')
    plt.title('ISS Positon')
    plt.show()

if __name__ == "__main__":

    print(get_astronauts())
    lat, lon = get_position()
    # lat, lon = -46.0879, -119.1377
    map_iss_position(lat, lon)
