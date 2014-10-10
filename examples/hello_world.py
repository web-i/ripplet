'''
A simple webi application, run by wsgi adaptor.
'''


def hello(environ):
  return 200, {'Content-Type': 'text/html'}, '<h3>Hello, from Ripple.</h3>'

if __name__ == '__main__':
  import ripple.adaptors
  from werkzeug.serving import run_simple
  run_simple('localhost', 4000, ripple.adaptors.wsgi(hello), use_debugger=True, use_reloader=True)
