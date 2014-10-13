'''
A simple webi application, run by wsgi adaptor.
'''
from ripple.middlewares import input

import cgi, io

def input_app(environ):
    environ_copy = environ.copy()
    if environ['REQUEST_METHOD'] in ('POST', 'PUT'):
      length = int(environ.get('CONTENT_LENGTH', '0'))
      environ['data'] = data = environ['wsgi.input'].read(length)
      data_input = cgi.FieldStorage(fp=io.BytesIO(data), environ=environ, keep_blank_values=True, encoding='utf8')
      environ['input'] = {key: process_fieldstorage(data_input[key]) for key in data_input.keys()}
    else:
      query_input = cgi.FieldStorage(environ=environ, keep_blank_values=True)
      environ['input'] = {key: process_fieldstorage(query_input[key]) for key in query_input.keys()}
    content = '''
    %s

    <form method="post">
      <input type="text" name="project" value="ripple">
      <input type="submit" name="input" value="input">
    </form>
    ''' % environ

    return 200, {'Content-Type': 'text/html'}, content



if __name__ == '__main__':
  import ripple.adaptors
  from werkzeug.serving import run_simple
  run_simple('localhost', 8000, ripple.adaptors.wsgi(input_app), use_debugger=True, use_reloader=True)
