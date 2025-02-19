import cherrypy

class HelloWorld:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        return "Yes oh"

if __name__ == "__main__":
    cherrypy.config.update({
        'server.socket_host': '127.0.0.1',  # Bind to localhost
        'server.socket_port': 8080,        # Run on port 8080
    })
    cherrypy.quickstart(HelloWorld())