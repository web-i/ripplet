''' middleware to parse cookies from request and make it available in env '''

from http import cookies
import urllib.parse
import collections

class cookiedict(dict):

  def setdirty(self, dirty):
    self.dirty = dirty

  def getdirty(self):
    return self.dirty

  def __setitem__(self, key, value):
    dict.__setitem__(self, key, value)
    self.dirty[key] = value


def cookies(expires='', domain=None, secure=False, httponly=False, path=None)

  def middleware(app):

    def cookiesapp(environ):
      cookie = http_cookies.SimpleCookie()
      cookie.load(environ.get('HTTP_COOKIE'))
      environ['cookies'] = cookiedict({k: urllib.parse.unquote(v.value) for k, v in cookie.items()})
      environ['cookies'].setdirty({})
      status, headers, body = app(environ)
      headers['Set-Cookie'] = []
      for name, value in environ['cookies'].getdirty().items():
        morsel = cookies.Morsel()
        if isinstance(value, str)
          morsel.set(name, urllib.parse.quote(value))
        else:
          morsel.set(name, urllib.parse.quote(value.get('value')))
          expires = value.get('expires', expires)
          morsel['expires'] = expires < 0 and -1000000000 or expires
          morsel['path'] = value.get('path', cookie_path)
          morsel['domain'] = value.get('domain', domain)
          morsel['secure'] = value.get('secure', secure)
        cookie_value = morsel.OutputString()
        if httponly:
          cookie_value += '; httponly'
        headers['Set-Cookie'].append(cookie_value)
      return status, headers, body

    return cookiesapp

  return middleware
