''' a composer to combine several middlewares for webi application '''

import functools

def builder(app, *middlewares):
  middleware_list = list(middlewares)
  middleware_list.reverse()
  middleware_list.append(app)
  return functools.reduce(lambda app1, app2: app1(app2), middleware_list)
