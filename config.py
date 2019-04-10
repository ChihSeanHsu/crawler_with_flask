# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:29:47 2019

@author: Sean
"""

class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True