#!/usr/bin/python
# -*- coding: utf-8 -*-
## Copyright (c) 2017, The Sumokoin Project (www.sumokoin.org)
'''
App top-level settings
'''

__doc__ = 'default application wide settings'

import sys
import os
import logging

from utils.common import getHomeDir, makeDir

USER_AGENT = "Dero GUI Wallet"
APP_NAME = "Dero Wallet"
VERSION = [0, 0, 2]
APP_TITLE = "%s v%d.%d.%d" % (APP_NAME, VERSION[0], VERSION[1],VERSION[2])

_data_dir = makeDir(os.path.join(os.getcwd(), 'data'))
DATA_DIR = _data_dir

log_file  = os.path.join(DATA_DIR, 'logs', 'app.log') # default logging file
log_level = logging.DEBUG # logging level

seed_languages = [("0", "German"), 
                  ("1", "English"),
                  ("2", "Spanish"),
                  ("3", "Francais"),
                  ("4", "Italian"),
                  ("5", "Dutch"),
                  ("6", "Portuguese"),
                  ("7", "Russian"),
                  ("8", "Japanese"),
                  ("9", "Chinese"),
                  ("10", "Esperanto"),
                ]

# COIN - number of smallest units in one coin
COIN = 1000000000000.0
WALLET_DAEMON_PORT = 18090
RPC_DAEMON_PORT = 18091
