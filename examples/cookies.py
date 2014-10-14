from ripple.middlewares import cookies
import random

def cookie_app(environ):
  got_cookie = environ['cookies'].get('cookie')
  environ['cookies']['cookie'] = random.randrange(100)
  return 200, {'Content-Type': 'text/html'}, environ['cookies']

if __name__ == '__main__':
  import ripple.adaptors
  from werkzeug.serving import run_simple
  run_simple('localhost', 8000, ripple.adaptors.wsgi(cookies()(cookie_app)), use_debugger=True, use_reloader=True)
