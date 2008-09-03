"""Open Library Books API
"""

from infogami.plugins.api.code import add_hook
import dynlinks

import web
from infogami.infobase import _json as simplejson

class books:
    def GET(self):
        i = web.input(bibkeys='', callback=None)
        result = simplejson.dumps(dynlinks.get_multi(i.bibkeys.split(',')), indent=4);
        web.ctx.headers = []
        web.header('Content-Type', 'text/javascript')
        if i.callback:
            return '%s(%s);' % (i.callback, result)
        else:
            return 'var _OLBookInfo = %s;' % result

add_hook("books", books)

