''' a middleware to serve static files from a configured directory'''
__all__ = ['static']

import os
import urllib.parse
from .file import file

def forbidden():
  return 403, {'Content-Type': 'text/html'}, '<html><body><h2>Forbidden</h2></body></html>'

def success(file):
  return 200, {}, file

def static(public_dir='public'):
  ''' a middleware that takes parameters and returns another middleware'''
  root = os.path.abspath(public_dir) + os.sep
  def static_middleware(app):
    def static_app(environ):
      uri = urllib.parse.unquote(environ['PATH_INFO'])[1:]
      filename, ext = os.path.splitext(uri)
      if uri == '' or uri[-1] == '/':
        uri += 'index.html'
      elif ext:
        pass
      else:
        uri += '.html'
      filename = os.path.abspath(os.path.join(root, uri.strip('/\\')))
      if uri.startswith(public_dir) or '..' in uri : return forbidden()
      try:
        file_handle = open(filename, 'rb')
        return success(file_handle)
      except:
        return app(environ)
    return static_app
  return static_middleware

