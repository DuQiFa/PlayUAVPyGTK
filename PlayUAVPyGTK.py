#!/usr/bin/python
#
# Configuration tool for PlayUAVOSD
#

import sys
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from gi.repository import GLib
from gi.repository import Gio


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

    """ Callback exiting program """
    def quit_callback(self, action, parameter):
        sys.exit()

    """ Start the application """
    def do_startup(self):
        Gtk.Application.do_startup(self)
        """ Load XML definitions of UI elements """
        builder = Gtk.Builder()
        try:
            builder.add_from_file("PlayUAVMenubar.ui")
        except:
            print("ui file not found")
            sys.exit()

        menubar = builder.get_object("menubar")
        self.set_menubar(menubar)

        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.quit_callback)
        self.add_action(quit_action)

app = PlayUAVApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
