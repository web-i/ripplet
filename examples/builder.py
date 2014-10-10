from ripple import builder
from ripple.middlewares import params, file_info
from ripple.adaptors import wsgi

def app_to_build(environ):
  return 200, {'Content-Type': 'text/html'}, open('builder.py', 'rb')

app = builder(app_to_build, file_info)

if __name__ == '__main__':
  from werkzeug.serving import run_simple
  run_simple('localhost', 4000, wsgi(app), use_debugger=True, use_reloader=True)
