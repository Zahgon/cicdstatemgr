#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

import base64
import yaml
import json
from jinja2 import Environment

def createEnvironment() -> Environment:
    env = Environment(extensions=['jinja2.ext.loopcontrols'])
    env.filters['to_nice_yaml'] = to_nice_yaml
    env.filters['from_json'] = from_json
    env.filters['json_dumps'] = json_dumps
    env.filters['kv_comma_pairs_to_json'] = kv_comma_pairs_to_json
    env.filters['to_base64'] = to_base64
    return env
    
# Jinja filter
def json_dumps(value,indent=None,stripLeadingTrailingQuotes=False):
    pass

# Jinja filter
def from_json(value):
    pass

# Jinja filter
def to_nice_yaml(value, default_flow_style=False, sort_keys=False, indent=2):
    pass

# Jinja filter
def kv_comma_pairs_to_json(value):
    pass

# Jinja filter
def to_base64(value):
    pass


