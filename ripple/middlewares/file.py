__all__ = ['file']

import mimetypes

def file(app):
  def _file_app(environ):
    status, headers, body = app(environ)
    if hasattr(body, 'read'):
      mimetype, encoding = mimetypes.guess_type(body.name)
      if encoding: headers['Content-Encoding'] = encoding
      if mimetype: headers['Content-Type'] = mimetype
    return status, headers, body
  return _file_app
