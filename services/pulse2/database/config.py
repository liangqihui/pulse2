#!/usr/bin/python
# -*- coding: utf-8; -*-
#
# (c) 2004-2007 Linbox / Free&ALter Soft, http://linbox.com
# (c) 2007 Mandriva, http://www.mandriva.com/
#
# $Id: __init__.py 195 2007-09-10 08:20:59Z cedric $
#
# This file is part of Mandriva Management Console (MMC).
#
# MMC is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# MMC is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MMC; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

# Misc
import ConfigParser
import re
import logging

# MMC
import mmc.support.mmctools
from pulse2.utils import Singleton, Pulse2ConfigParser

class DatabaseConfig(Pulse2ConfigParser):
    dbsection = "database"
    
    dbdriver = 'mysql'
    dbhost = "127.0.0.1"
    dbname = None
    dbport = None
    dbuser = 'mmc'
    dbpasswd = 'mmc'

    dbdebug = "ERROR"
    dbpoolrecycle = 60
    dbpoolsize = 5 
    # SSL support
    dbsslenable = False
    dbsslca = None
    dbsslcert = None
    dbsslkey = None

    def setup(self, config_file):
        # Load configuration file
        self.cp = Pulse2ConfigParser()
        self.cp.read(config_file)
                                
        if self.cp.has_section(self.dbsection):
            if self.cp.has_option(self.dbsection, "dbdriver"):
                self.dbdriver = self.cp.get(self.dbsection, "dbdriver")
            if self.cp.has_option(self.dbsection, "dbhost"):
                self.dbhost = self.cp.get(self.dbsection, "dbhost")
            if self.cp.has_option(self.dbsection, "dbname"):
                self.dbname = self.cp.get(self.dbsection, "dbname")
            if self.cp.has_option(self.dbsection, "dbuser"):
                self.dbuser = self.cp.get(self.dbsection, "dbuser")
            if self.cp.has_option(self.dbsection, "dbpasswd"):
                self.dbpasswd = self.cp.getpassword(self.dbsection, "dbpasswd")

            if self.cp.has_option(self.dbsection, "dbdebug"):
                self.dbdebug = self.cp.get(self.dbsection, "dbdebug")
                        
            if self.cp.has_option(self.dbsection, "dbpoolrecycle"):
                self.dbpoolrecycle = self.cp.getint(self.dbsection, "dbpoolrecycle")

            if self.cp.has_option(self.dbsection,  "dbpoolsize"):
                self.dbpoolsize = self.cp.getint(self.dbsection, "dbpoolsize")

            if self.cp.has_option(self.dbsection, "dbsslenable"):
                self.dbsslenable = self.cp.getboolean(self.dbsection, "dbsslenable")
                if self.dbsslenable:
                    self.dbsslca = self.cp.get(self.dbsection, "dbsslca")
                    self.dbsslcert = self.cp.get(self.dbsection, "dbsslcert")
                    self.dbsslkey = self.cp.get(self.dbsection, "dbsslkey")

