''' a wsgi adaptor for webi application '''

from wsgiref.util import FileWrapper
status_codes = {
  200: 'OK',
  403: 'Forbidden',
}


def webi_2_wsgi_status(status):
  '''
  given an integer status code used by webi, return wsgi compatible status code with description
  >>> webi_2_wsgi_status(200)
  '200 OK'
  '''
  return '%d %s' % (status, status_codes[status])

def wsgi(webi_app):
  ''' webi to wsgi application adaptor '''
  def wsgi_app(environ, start_response):
    status, headers, body = webi_app(environ)
    wsgi_headers = []
    for header, value in headers.items():
      if isinstance(value, list):
        wsgi_headers += [(header, value_item) for value_item in value]
      else:
        wsgi_headers.append((header, value))
    wsgi_status = webi_2_wsgi_status(status)
    start_response(wsgi_status, wsgi_headers)
    if not body:
      if 'Content-Length' not in headers: headers['Content-Length'] = 0
      return []
    elif hasattr(body, 'read'):
      if 'wsgi.file_wrapper' in environ:
        return environ['wsgi.file_wrapper'](body)
      elif hasattr(body, 'close') or not hasattr(body, '__iter__'):
        return FileWrapper(body)
    elif isinstance(body, str):
      return [chunk.encode() for chunk in body]
    else:
      # string representation of other python types
      return [repr(body).encode()]
  return wsgi_app

if __name__ == '__main__':
  import doctest
  doctest.testmod()
