''' signed cookie based sessions '''
''' tested only for simple session key values (implementation/test for nested structures soon) '''

__all__ = ['sessions']

import base64
import json

def sessions(cookiename='ripple.session',
             cookiedomain = '',
             cookiepath = '/',
             expires = 24 * 60 * 60, # one day
             permanent = True,
             http_only = True,
             secure = False):
  if permanent: expires = 10 * 365 * expires # ten years of timeout :O

  def middleware(app):

    def encode(session_dict):
      return json.dumps(session_dict)

    def decode(session_string):
      return json.loads(session_string)

    def sessionapp(environ):
      session_cookie = environ['cookies'].get(cookiename, '')
      environ['session'] = session_cookie and decode(session_cookie) or {}
      session_copy = environ['session'].copy() # support for nested dicts soon
      status, headers, body = app(environ)
      if environ['session'] != session_copy:
        environ['cookies'][cookiename] = encode(environ['session'])
      return status, headers, body

    return sessionapp

  return middleware
