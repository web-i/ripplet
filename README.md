ripple: a meta web framework for python
======

`ripple` lets you write [`webi`](https://github.com/web-i/webi) applications. It is a collection of `webi` middlewares, utilities and web server adaptors.

`ripple` takes everything it can from clojure's `ring`, perl's `plack`, python's `werkezeug` and ruby's `rack`.

## installing ripple

> pip install webi-ripple

## running webi applications

Currently there are no direct interfaces to webservers. But you can use `wsgi` adaptor to convert webi applications to wsgi and run them with any wsgi compliant container.

Following example runs a sample app with werkezeug wsgi server.

```python
def hello(environ):
  return 200, {'Content-Type': 'text/html'}, '<h3>Hello, from Ripple.</h3>'

if __name__ == '__main__':
  import ripple.adaptors
  from werkzeug.serving import run_simple
  run_simple('localhost', 4000, ripple.adaptors.wsgi(hello), use_debugger=True, use_reloader=True)
```

## adding features using middlewares

Additional capabilities can be added to webi applications using included and contributed middlewares. A middleware takes a webi application, wraps additional functionality and returns a webi application.

Following example shows, how a webi can serve a file as a response body.
```python
from ripple.middlewares import file_info
import ripple.adaptors

def file(environ):
  return 200, {}, open('ripple.png', 'rb')

app = ripple.adaptors.wsgi(file_info(file))
```
## composing a webi app

ripple provides `builder`, a helper function to compose middlewares for application. It can be used as a following.

```python
from ripple import builder
import ripple.middlewares

def basic(environ):
  return 200, {'Content-Type': 'text/plain'}, 'a composed app'

app =  builder(builder, ripple.middlewares.params, ripple.middlewares.file_info, ripple.middlewares.static)
```

