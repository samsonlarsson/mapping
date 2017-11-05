# encoding: utf-8

from mediadrop.lib.base import BaseController
from mediadrop.lib.decorators import expose

class SampleController(BaseController):
    @expose('mapping/map.html')
    def index(self, value=None, **kwargs):
        # do your backend work here
        # …
        return {'value': value}
