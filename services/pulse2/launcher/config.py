# -*- coding: utf-8; -*-
#
# (c) 2007-2008 Mandriva, http://www.mandriva.com/
#
# $Id$
#
# This file is part of Pulse 2, http://pulse2.mandriva.org
#
# Pulse 2 is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Pulse 2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pulse 2; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.


# Misc
import ConfigParser
import re

# MMC
import mmc.support.mmctools

class LauncherConfig(mmc.support.mmctools.Singleton):
    """
    Singleton Class to hold configuration directives

    """
    name = None
    pid_path = "/var/run/pulse2"
    launcher_path = "/usr/sbin/pulse2-launcher"
    wrapper_path = "/usr/sbin/pulse2-output-wrapper"
    source_path = "/tftpboot/revoboot/msc"
    target_path = "/tmp"
    inventory_command = "echo Doing inventory"
    launchers = {
        'launcher_01': {
            'port': 8001,
            'bind': '127.0.0.1',
            'slots': 300
        }
    }
    scheduler_host = "127.0.0.1"
    scheduler_port = "9000"
    awake_time = 600
    defer_results = False
    ssh_defaultkey = 'default'
    ssh_keys = { 'default': '/root/.ssh/id_dsa.pub' }
    ssh_options = [ \
        'StrictHostKeyChecking=no',
        'Batchmode=yes',
        'PasswordAuthentication=no',
        'SetupTimeOut=10',
        'ServerAliveInterval=10',
        'CheckHostIP=no',
        'ConnectTimeout=10'
    ]

    scp_options = [ \
        'StrictHostKeyChecking=no',
        'Batchmode=yes',
        'PasswordAuthentication=no',
        'SetupTimeOut=10',
        'ServerAliveInterval=10',
        'CheckHostIP=no',
        'ConnectTimeout=10'
    ]

    def setup(self, config_file, name):
        # Load configuration file
        cp = ConfigParser.ConfigParser()
        cp.read(config_file)

        self.name = name

        if cp.has_option("launchers", "pid_path"):
            self.pid_path = cp.get("launchers", "pid_path")
        if cp.has_option("launchers", "launcher_path"):
            self.launcher_path = cp.get("launchers", "launcher_path")
        if cp.has_option("launchers", "wrapper_path"):
            self.wrapper_path = cp.get("launchers", "wrapper_path")
        if cp.has_option("launchers", "source_path"):
            self.source_path = cp.get("launchers", "source_path")
        if cp.has_option("launchers", "target_path"):
            self.target_path = cp.get("launchers", "target_path")
        if cp.has_option("launchers", "inventory_command"):
            self.inventory_command = cp.get("launchers", "inventory_command")
        if cp.has_option("launchers", "temp_folder_prefix"):
            self.temp_folder_prefix = cp.get("launchers", "temp_folder_prefix")

        for section in cp.sections():
            if re.compile("^launcher_[0-9]+$").match(section):
                self.launchers[section] = {
                        'port': cp.get(section, "port"),
                        'bind': cp.get(section, "bind"),
                        'slots': cp.get(section, "slots")
                    }
        if cp.has_option("scheduler", "host"):
            self.scheduler_host = cp.get("scheduler", "host")
        if cp.has_option("scheduler", "port"):
            self.scheduler_port = cp.get("scheduler", "port")
        if cp.has_option("scheduler", "awake_time"):
            self.awake_time = cp.getint("scheduler", "awake_time")
        if cp.has_option("scheduler", "defer_results"):
            self.defer_results = cp.get("scheduler", "defer_results") == 'yes'

        for option in cp.options('ssh'):
            if re.compile("^sshkey_[0-9A-Za-z]+$").match(option):
                keyname = re.compile("^sshkey_([0-9A-Za-z]+)$").match(option).group(1)
                self.ssh_keys[keyname] = cp.get('ssh', option)
        if cp.has_option("ssh", "default_key"):
            self.ssh_defaultkey = cp.get("ssh", "default_key")
        if cp.has_option("ssh", "ssh_options"):
            self.ssh_options = cp.get("ssh", "ssh_options").split(' ')
        if cp.has_option("ssh", "scp_options"):
            self.scp_options = cp.get("ssh", "scp_options").split(' ')



