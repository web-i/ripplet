__all__ = ['input', 'middleware']

''' a middleware to build http params '''

'''#makingitpossible no file uploads handled yet '''

import io, cgi, collections

def middleware(app):

  def process_fieldstorage(fieldstorage):
    ''' not processing file uploads '''
    return isinstance(fieldstorage, list) and [process_fieldstorage(fs) for fs in fieldstorage] or fieldstorage.value

  def input_app(environ):
    if environ['REQUEST_METHOD'] in ('POST', 'PUT'):
      length = int(environ.get('CONTENT_LENGTH', '0'))
      environ['data'] = data = environ['wsgi.input'].read(length)
      data_input = cgi.FieldStorage(fp=io.BytesIO(data), environ=environ, keep_blank_values=True, encoding='utf8')
      environ['input'] = {key: process_fieldstorage(data_input[key]) for key in data_input.keys()}
    else:
      query_input = cgi.FieldStorage(environ=environ, keep_blank_values=True)
      environ['input'] = {key: process_fieldstorage(query_input[key]) for key in query_input.keys()}
    return app(environ)
  return input_app

def input():
  return middleware
