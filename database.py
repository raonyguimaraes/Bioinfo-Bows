#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import MySQLdb.cursors

#connect to the database
conn = MySQLdb.connect (host = "biodados.icb.ufmg.br",
                        user = "bows",
                        passwd = "bows123",
                        db = "bows",
                        cursorclass = MySQLdb.cursors.DictCursor)
cursor = conn.cursor()
