'''
A webi for serving static directory.
'''
from ripple.middlewares import static, file_info
import ripple.adaptors

def dynamic(environ):
  return 200, {}, '<html><body>not a static</body></html>'

if __name__ == '__main__':
  from werkzeug.serving import run_simple
  run_simple('localhost', 4000, ripple.adaptors.wsgi(file_info(static()(dynamic))), use_debugger=True, use_reloader=True)
