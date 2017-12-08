#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__=""

from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import text

app = Sanic('some_name')

class SimpleView(HTTPMethodView):

  def get(self, request):
      return text('I am get method')

  def post(self, request):
      return text('I am post method')

  def put(self, request):
      return text('I am put method')

  def patch(self, request):
      return text('I am patch method')

  def delete(self, request):
      return text('I am delete method')

app.add_route(SimpleView.as_view(), '/')

def a(func):
    def wrap(a):
        print("a")
        r = func(a)
        return r
    return wrap
class ViewWithDecorator(HTTPMethodView):
  decorators = [a]

  def get(self, request):
    return text('Hello I have a decorator')

app.add_route(ViewWithDecorator.as_view(), '/url')
app.run()