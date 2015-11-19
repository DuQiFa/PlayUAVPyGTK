#!/usr/bin/python
#
# Configuration tool for PlayUAVOSD
#

import sys
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk


class PlayUAVWindow(Gtk.ApplicationWindow):
    """ Constructor for application window """
    def __init__(self, app):
        Gtk.Window.__init__(self, title="PlayUAVOSD", application=app)
        self.set_default_size(800, 600)


class PlayUAVApplication(Gtk.Application):
    """ Constructor for Gtk.Application """

    def __init__(self):
        Gtk.Application.__init__(self)

    """ Create an active PlayUAVWindow """
    def do_activate(self):
        win = PlayUAVWindow(self)
        win.show_all()

    """ Start the application """
    def do_startup(self):
        Gtk.Application.do_startup(self)

app = PlayUAVApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
