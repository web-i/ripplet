''' signed cookie based sessions '''
''' tested only for simple session key values (implementation/test for nested structures soon) '''

__all__ = ['sessions']

import base64
import json

def sessions(cookiename='ripple.session.id',
             cookiedomain = None,
             cookiepath = None,
             expires = 24 * 60 * 60, # one day
             permanent = True,
             http_only = True,
             secure = True):
  if permanent: timeout = 10 * 365 * timeout # ten years of timeout :O

  def middleware(app):

    def encode(session_dict):
      jsoned = json.dumps(session_dict)
      return base64.encodestring(jsoned.encode())

    def decode(session_string):
      jsoned = base64.decodestring(session_string.decode())
      return json.loads(jsoned)

    def sessionapp(environ):
      session_cookie = environ['cookies'].get(cookiename, '')
      environ['session'] = session_cookie and decodestring(session_cookie) or {}
      session_copy = environ['session'].copy() # support for nested dicts soon
      status, headers, body = app(environ)
      if environ['session'] != session_copy:
        sessioncookie = {
          'value': encode(environ['session']),
          'expires': expires,
          'path': cookiepath,
          'domain': cookiedomain,
          'secure': secure,
          'http_only': http_only
        }
        environ['cookies'][cookiename] = sessioncookie
      return status, headers, body

    return sessionapp

  return middleware
