from wsgiref.util import FileWrapper
status_codes = {
  200: 'OK'
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
    start_response(webi_2_wsgi_status(status), [(header, value) for header, value in headers.items()])
    if not body:
      if 'Content-Length' not in headers: headers['Content-Length'] = 0
      return []
    elif hasattr(body, 'read'):
      if 'wsgi.file_wrapper' in environ:
        return environ['wsgi.file_wrapper'](body)
      elif hasattr(body, 'close') or not hasattr(body, '__iter__'):
        return FileWrapper(body)
    elif isinstance(body[0], str):
      return [chunk.encode() for chunk in body]
  return wsgi_app

if __name__ == '__main__':
  import doctest
  doctest.testmod()
