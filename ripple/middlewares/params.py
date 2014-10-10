''' a middleware to build http params '''

def params(app):
  def params_app(environ):
    return app(environ)
  return params_app
