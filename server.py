import falcon
import os
from wsgiref import simple_server

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.


class ThingsResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nAufklärung ist der Ausgang des Menschen aus seiner selbstverschuldeten Unmündigkeit'
                     '\n'
                     '    ~ Immanuel Kant\n\n')


# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()

# things will handle all requests to the '/things' URL path
app.add_route('/', things)

if __name__ == '__main__':
    PORT = os.getenv("PORT", 8000)
    httpd = simple_server.make_server('0.0.0.0', int(PORT), app)
    httpd.serve_forever()
