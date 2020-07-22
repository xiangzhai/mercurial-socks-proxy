# -*- coding: utf-8 -*-
#
# Copyright 2014 Bug Heisen <heisenbug@zoho.com>
# Copyright 2020 Leslie Zhai <zhaixiang@loongson.cn>
#
# This extension enables SOCKS5 proxy support for Mercurial. You'll
# also need the PySocks socks.py module for this to work, as this
# implements the actual SOCKS protocol. Currently, only SOCKS5 is
# supported, without a username or password.
#
# This software may be used and distributed according to the terms of the
# GNU General Public License version 2 or any later version.

from mercurial import error
from mercurial.i18n import _
import socket
import socks

def uisetup(ui):

    proxyurl = ui.config(b"socks_proxy", b"host")

    if proxyurl:
        idx = proxyurl.find(b":")
        if idx < 0:
            raise error.Abort(_("host in socks_proxy should be "
                                "hostname:port"))

        host = proxyurl[:idx]
        portstr = proxyurl[idx+1:]
        try:
            port = int(portstr)
        except ValueError:
            raise error.Abort(_("Cannot interpret '%s' in the socks_proxy "
                                "host line as an integer port number")
                                % portstr)

        if port <= 0 or port > 65535:
           raise error.Abort(_("Port number in socks_proxy host line "
                               "must lie between 1 and 65535, but is %d")
                               % port)

        try:
            socks.set_default_proxy(socks.SOCKS5, host, port)
            socket.socket = socks.socksocket
        except ImportError:
            raise error.Abort(_("The SocksiPy socks module is needed for "
                                "SOCKS support"))
