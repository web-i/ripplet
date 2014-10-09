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
    return [chunk.encode() for chunk in body]
  return wsgi_app

if __name__ == '__main__':
  import doctest
  doctest.testmod()
