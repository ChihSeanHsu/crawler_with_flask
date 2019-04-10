# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:31:49 2019

@author: Sean
"""

from flask_script import Manager, Server
from main import app

manager = Manager(app)

manager.add_command('runserver', Server())

@manager.shell
def make_shell_context():
    return dict(app=app)

if __name__ == '__main__':
    manager.run()