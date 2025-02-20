import cherrypy

class HelloWorld:
    @cherrypy.expose
    def img(self):
        cherrypy.response.headers['Content-Type'] = 'text/html'
        return 
        """
        <html>
            <body>
                <h1>Hello, World!</h1>
                <img src="/static/image.jpg" alt="Sample Image">
            </body>
        </html>
        """

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        telex_json = {
            "data": {
                "date": {
                "created_at": "2024-02-20",
                "updated_at": "2024-02-20"
                },
                "descriptions": {
                    "app_description": "A real time error log for CherryPy framework that captures and reports errors and exceptions occurring in a CherryPy application.",
                    "app_logo": "http://137.184.27.66/static/logo.svg",
                    "app_name": "Errorless Cherry",
                    "app_url": "URL to the application or service.",
                    "background_color": "#E3E1E6"
                },
                "integration_category": "Communication & Collaboration",
                "integration_type": "output",
                "is_active": False,
                "output": [
                {
                    "label": "output_channel_1",
                    "value": True
                },
                {
                    "label": "output_channel_2",
                    "value": False,
                }
                ],
                "key_features": [
                "Checks for unhandled error",
                "Logs error in your app",
                "Forwards this error to Telex",
                "Forwards to your developer's forum"
                ],
                "permissions": {
                "monitoring_user": {
                    "always_online": True,
                    "display_name": "Performance Monitor"
                }
                },
                "settings": [
                {
                    "label": "Do you want to continue",
                    "type": "checkbox",
                    "required": True,
                    "default": "Yes"
                },
                ],
                "tick_url": "URL for subscribing to Telex's clock.",
                "target_url": "Optional URL for getting data from the Telex channel"
            }
        }

        return telex_json

if __name__ == "__main__":
    cherrypy.config.update({
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 8080,
    })

    config = {
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '/',
        }
    }

    cherrypy.quickstart(HelloWorld(), '/', config)