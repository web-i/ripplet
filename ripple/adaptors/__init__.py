def wsgi(webi_app):
  def wsgi_app(environ, start_response):
    status, headers, body = webi_app(environ)
    start_response(status, [(header, value) for header, value in headers.items()])
    return body
  return wsgi_app
