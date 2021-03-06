
'''
The main server file
'''
from tornado.web import RequestHandler, Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import os
from uuid import uuid4
import torn

from routes import *
settings = dict(
		template_path=os.path.join(os.path.dirname(__file__),"public"),
		static_path=os.path.join(os.path.dirname(__file__),"static"),
		login_url="/login",
		cookie_secret=str(uuid4()),
		debug=torn.Debug(),
	)

application = Application(route, **settings)

if __name__ == "__main__":
	server = HTTPServer(application)
	server.listen(os.environ.get('PORT'))
	IOLoop.current().start()

					
