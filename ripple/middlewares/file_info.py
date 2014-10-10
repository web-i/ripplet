''' a middleware to add content-type header for file responses'''
__all__ = ['file']

import mimetypes

def file_info(app):
  def file_info_app(environ):
    status, headers, body = app(environ)
    if hasattr(body, 'read'):
      mimetype, encoding = mimetypes.guess_type(body.name)
      if encoding: headers['Content-Encoding'] = encoding
      if mimetype: headers['Content-Type'] = mimetype
    return status, headers, body
  return file_info_app
