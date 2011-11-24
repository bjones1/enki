"""
helpmenu --- Help main menu items. Aboout dialogue
==================================================

About dialogue and *Help* menu items
"""

import os.path

from PyQt4 import uic
from PyQt4.QtCore import QObject
from PyQt4.QtGui import qApp, QDialog, QIcon

from mks.core.defines import PACKAGE_NAME, PACKAGE_VERSION
from mks.core.core import core, DATA_FILES_PATH

class Plugin(QObject):
    """Module implementation
    """
    def __init__(self):
        QObject.__init__(self)
        
        def createAction(menuItem, text, icon, tab):
            """Create a menu action and connect it to the slot
            """
            action = core.actionModel().addAction("mHelp/%s" % menuItem, text, QIcon(':mksicons/' + icon))
            slot = lambda : UIAbout(core.mainWindow(), tab).exec_()  # pylint: disable=W0108
            action.triggered.connect(slot)
        
        createAction('aAbout', self.tr('&About...'), 'monkey2.png', 'about')
        createAction('aHelp', self.tr('&Help...'), 'help.png', 'help')
        createAction('aReportBug', self.tr('Report &Bug...'), 'debugger.png', 'bug')
        createAction('aDonate', self.tr('&Donate...'), 'add.png', 'donate')

        action = core.actionModel().addAction( "mHelp/aAboutQt", self.tr('About &Qt...'), QIcon(':mksicons/qt.png'))
        action.triggered.connect(qApp.aboutQt)

    def moduleConfiguratorClass(self):
        """ ::class:`mks.core.uisettings.ModuleConfigurator` used to configure plugin with UISettings dialogue
        """
        return None  # No any settings

class UIAbout(QDialog):
    """About dialogue
    """
    def __init__(self, parentWindow, tab):
        QDialog.__init__(self, parentWindow)
        uic.loadUi(os.path.join(DATA_FILES_PATH, 'ui/UIAbout.ui'), self)
        self.setWindowTitle( self.tr( "About : %s" % PACKAGE_NAME ) )
        
        self.lTitle.setText( PACKAGE_NAME )
        self.lVersion.setText( self.tr( "Version %s" % PACKAGE_VERSION ))
        
        tabs = {'about': self.wLogo,
                'help': self.tbHelp,
                'bug': self.tbReportBug,
                'donate': self.tbDonations}        
        self.twAbout.setCurrentWidget(tabs[tab])
