'''
A simple webi application, run by wsgi adaptor.
'''
import ripple.adaptors

def hello(environ):
  return 200, {'Content-Type': 'text/html'}, '<h3>Hello, from Ripple.</h3>'

if __name__ == '__main__':
  from wsgiref.simple_server import make_server
  httpd = make_server('', 8000, ripple.adaptors.wsgi(hello))
  httpd.serve_forever()
