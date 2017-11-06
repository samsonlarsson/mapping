# encoding: utf-8

from mediadrop.lib.base import BaseController
from mediadrop.lib.decorators import expose

import googlemaps

gmaps = googlemaps.Client(key='AIzaSyA3mWehI-WUOmQlTs7h5sV339EcL484DHQ')

# Geo-coding an address
geocode_result = gmaps.geocode('Siera Leone & Liberia')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((7.493196470122287, -10.1953125))


class MapController(BaseController):
    @expose('mapping/map.html')
    def index(self, value=None, **kwargs):
        # do your backend work here
        # …
        return {'value': value}
