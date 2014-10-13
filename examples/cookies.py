from http import cookies as http_cookies
import urllib.parse

def cookies(environ):
  cookie = http_cookies.SimpleCookie()
  cookie.load(environ.get('HTTP_COOKIE'))
  environ['cookies'] = {k: urllib.parse.unquote(v.value) for k, v in cookie.items()}

  return 200, {'Content-Type': 'text/html'}, environ['cookies']

if __name__ == '__main__':
  import ripple.adaptors
  from werkzeug.serving import run_simple
  run_simple('localhost', 8000, ripple.adaptors.wsgi(cookies), use_debugger=True, use_reloader=True)
