from ripple.middlewares import cookies
from ripple.middlewares import sessions
import random

def session_app(environ):
  got_session = environ['session'].get('session')
  environ['cookies']['cookie'] = environ['session']['session'] = random.randrange(100)

  return 200, {'Content-Type': 'text/html'}, str(got_session) +'|'+ str(environ['session']['session'])

if __name__ == '__main__':
  import ripple.adaptors
  from werkzeug.serving import run_simple
  run_simple('localhost', 8000, ripple.adaptors.wsgi(cookies()(sessions()(session_app))), use_debugger=True, use_reloader=True)


