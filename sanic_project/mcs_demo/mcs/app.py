#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __datetime__
# __purpose__

"""The app module, containing the app factory function."""
from sanic import Sanic

class Init_app:
    def __init__(self):
        pass
    """
    init_app
    """
    def create_app(self):
        app = Sanic(__name__)
        self.register_app(app)
        return app


    """
    register_app
    """
    def register_app(self,app):
        """import bp"""
        from mcs import reshell
        app.blueprint(reshell.view.reshell)