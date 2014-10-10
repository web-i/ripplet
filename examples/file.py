'''
A webi for serving file.
'''
from ripple.middlewares import file_info
import ripple.adaptors

def hello(environ):
  return 200, {}, open('static/ripple.png', 'rb')

if __name__ == '__main__':
  from werkzeug.serving import run_simple
  run_simple('localhost', 4000, ripple.adaptors.wsgi(file_info((hello)), use_debugger=True, use_reloader=True)
