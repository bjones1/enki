from PyQt4.QtCore import Qt
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtCore import QString
from PyQt4.QtCore import QSize
from PyQt4.QtGui import qApp
from PyQt4.QtGui import QIcon
from PyQt4.QtGui import QDockWidget

from PyQt4.fresh import pMainWindow

import mks.monkeycore


class MainWindow(pMainWindow):
    
    aboutToClose = pyqtSignal()
    urlsDropped = pyqtSignal()
    
    def __init__(self):
        pMainWindow.__init__(self)
        """TODO
        self.setUnifiedTitleAndToolBarOnMac( True )
        self.setIconSize( QSize( 16, 16 ) )
        self.setAcceptDrops( True )
        
        self.setCorner( Qt.TopLeftCorner, Qt.LeftDockWidgetArea )
        self.setCorner( Qt.TopRightCorner, Qt.RightDockWidgetArea )
        self.setCorner( Qt.BottomLeftCorner, Qt.LeftDockWidgetArea )
        self.setCorner( Qt.BottomRightCorner, Qt.RightDockWidgetArea )
        """
    
    def initGui(self):
        # init menubar
        self.initMenuBar()
        """TODO
        # init recents manager
        mks.monkeycore.recentsManager()
        # init toolbar
        self.initToolBar()
        """
        # init workspace
        self.setCentralWidget( mks.monkeycore.workspace() )
        """TODO
        # init message toolbar
        messageTb =  mks.monkeycore.messageManager()
        messageTb.setObjectName( "pQueuedMessageToolBar" )
        messageTb.setVisible( False )
        messageTb.setDefaultPixmap( mks.iconmanager.pixmap( "messages_infos.png", ":/messages" ) )
        pMonkeyStudio.setMacSmallSize( messageTb, true, true )
        self.centralWidget().layout().setMenuBar( messageTb )
        # init projects manager
        dockToolBar( Qt.LeftToolBarArea ).addDock( mks.monkeycore.projectsManager(), mks.monkeycore.projectsManager().windowTitle(), QIcon( ":/project/icons/project/project.png" ) )
        """
        # init opened files dock
        openedFileExplorer = mks.monkeycore.workspace().dockWidget()
        self.dockToolBar( Qt.LeftToolBarArea ).addDock( openedFileExplorer, openedFileExplorer.windowTitle(), openedFileExplorer.windowIcon() )
        """ TODO
        # init multitoolbar
        mks.monkeycore.workspace().initMultiToolBar( mks.monkeycore.multiToolBar().toolBar( pWorkspace.defaultContext() ) )
        mks.monkeycore.workspace().initMultiToolBar( mks.monkeycore.multiToolBar().toolBar( "Coding" ) )
        # init status bar
        setStatusBar( mks.monkeycore.statusBar() )
        # init connection
        """
        self.initConnections()
        mks.monkeycore.workspace().openFile('/home/a/tmp/1') # FIXME

    def initMenuBar(self):
        # create menubar menus and actions
        mb = self.menuBar()
        
        mb.setDefaultShortcutContext( Qt.ApplicationShortcut )
        
        mb.menu( "mFile", self.tr( "File" ) )
        mb.beginGroup( "mFile" )
        """TODO
        mb.action( "aNew", self.tr( "&New..." ), QIcon( ":/file/icons/file/new.png" ), self.tr( "Ctrl+N" ), self.tr( "Create a new file" ) )
        mb.action( "aNewTextEditor", self.tr( "&New Text File..." ), QIcon( ":/file/icons/file/new.png" ), '', self.tr( "Quickly create a new text based file" ) )
        """
        mb.action( "aOpen", self.tr( "&Open..." ), QIcon( ":/file/icons/file/open.png" ), self.tr( "Ctrl+O" ), self.tr( "Open a file" ) )
        """TODO
        mb.menu( "mRecents", self.tr( "&Recents" ), QIcon( ":/file/icons/file/recents.png" ) )
        mb.action( "mRecents/aClear", self.tr( "&Clear" ), QIcon( ":/file/icons/file/clear.png" ), '', self.tr( "Clear the recents files list" ) )
        mb.action( "mRecents/aSeparator1" )
        mb.action( "aSeparator1" )
        mb.menu( "mSession", self.tr( "Session" ), QIcon( ":/file/icons/file/session.png" ) )
        mb.action( "mSession/aSave", self.tr( "Save" ), QIcon( ":/file/icons/file/save.png" ), '', self.tr( "Save the current session files list" ) )
        mb.action( "mSession/aRestore", self.tr( "Restore" ), QIcon( ":/file/icons/file/restore.png" ), '', self.tr( "Restore the current session files list" ) )
        mb.action( "aSeparator2" )
        """
        mb.menu( "mSave", self.tr( "&Save" ), QIcon( ":/file/icons/file/save.png" ) )
        mb.action( "mSave/aCurrent", self.tr( "&Save" ), QIcon( ":/file/icons/file/save.png" ), self.tr( "Ctrl+S" ), self.tr( "Save the current file" ) ).setEnabled( False )
        mb.action( "mSave/aAll", self.tr( "Save &All" ), QIcon( ":/file/icons/file/saveall.png" ), '', self.tr( "Save all files" ) ).setEnabled( False )
        """TODO
        mb.menu( "mClose", self.tr( "&Close" ), QIcon( ":/file/icons/file/close.png" ) )
        mb.action( "mClose/aCurrent", self.tr( "&Close" ), QIcon( ":/file/icons/file/close.png" ), self.tr( "Ctrl+W" ), self.tr( "Close the current file" ) ).setEnabled( False )
        mb.action( "mClose/aAll", self.tr( "Close &All" ), QIcon( ":/file/icons/file/closeall.png" ), '', self.tr( "Close all files" ) ).setEnabled( False )
        mb.action( "aSeparator3" )
        mb.action( "aReload", self.tr( "Reload" ), QIcon( ":/file/icons/file/reload.png" ), '', self.tr( "Reload the current file asking user confirmation if needed" ) ).setEnabled( False )
        mb.action( "aSaveAsBackup", self.tr( "Save As &Backup" ), QIcon( ":/file/icons/file/backup.png" ), '', self.tr( "Save a backup of the current file" ) ).setEnabled( False )
        mb.action( "aSeparator4" )
        mb.action( "aQuickPrint", self.tr( "Quic&k Print" ), QIcon( ":/file/icons/file/quickprint.png" ), '', self.tr( "Quick print the current file" ) ).setEnabled( False )
        mb.action( "aPrint", self.tr( "&Print..." ), QIcon( ":/file/icons/file/print.png" ), self.tr( "Ctrl+P" ), self.tr( "Print the current file" ) ).setEnabled( False )
        mb.action( "aSeparator5" )
        mb.action( "aQuit", self.tr( "&Quit" ), QIcon( ":/file/icons/file/quit.png" ), self.tr( "Ctrl+Q" ), self.tr( "Quit the application" ) )
        """
        mb.endGroup()
        
        
        mb.menu( "mEdit", self.tr( "Edit" ) )
        mb.beginGroup( "mEdit" )
        """TODO
        mb.action( "aSettings", self.tr( "Settings..." ), QIcon( ":/edit/icons/edit/settings.png" ), "", self.tr( "Edit the application settings" ) )
        mb.action( "aShortcutsEditor", self.tr( "Shortcuts Editor..." ), QIcon( ":/edit/icons/edit/shortcuts.png" ), self.tr( "Ctrl+Shift+E" ), self.tr( "Edit the application shortcuts" ) )
        mb.action( "aTranslations", self.tr( "Translations..." ), QIcon( ":/edit/icons/edit/translations.png" ), self.tr( "Ctrl+T" ), self.tr( "Change the application translations files" ) )
        mb.action( "aSeparator1" )
        """
        mb.action( "aUndo", self.tr( "&Undo" ), QIcon( ":/edit/icons/edit/undo.png" ), self.tr( "Ctrl+Z" ), self.tr( "Undo" ) ).setEnabled( False )
        mb.action( "aRedo", self.tr( "&Redo" ), QIcon( ":/edit/icons/edit/redo.png" ), self.tr( "Ctrl+Y" ), self.tr( "Redo" ) ).setEnabled( False )
        mb.action( "aSeparator2" )
        mb.action( "aCopy", self.tr( "&Copy" ), QIcon( ":/edit/icons/edit/copy.png" ), self.tr( "Ctrl+C" ), self.tr( "Copy" ) ).setEnabled( False )
        mb.action( "aCut", self.tr( "Cu&t" ), QIcon( ":/edit/icons/edit/cut.png" ), self.tr( "Ctrl+X" ), self.tr( "Cut" ) ).setEnabled( False )
        mb.action( "aPaste", self.tr( "&Paste" ), QIcon( ":/edit/icons/edit/paste.png" ), self.tr( "Ctrl+V" ), self.tr( "Paste" ) ).setEnabled( False )
        mb.action( "aSeparator3" )
        """TODO
        mb.menu( "mSearchReplace", self.tr( "&Search && Replace" ) )
        mb.action( "mSearchReplace/aSearchFile", self.tr( "&Search..." ), QIcon( ":/edit/icons/edit/search.png" ), self.tr( "Ctrl+F" ), self.tr( "Search in the current file..." ) )
        mb.action( "aGoTo", self.tr( "&Go To..." ), QIcon( ":/edit/icons/edit/goto.png" ), self.tr( "Ctrl+G" ), self.tr( "Go To..." ) ).setEnabled( False )
        mb.menu( "mAllCommands", self.tr( "&All Commands" ), QIcon( ":/edit/icons/edit/commands.png" ) )
        mb.menu( "mBookmarks", self.tr( "&Bookmarks" ), QIcon( ":/editor/bookmark.png" ) )
        mb.action( "aSeparator5" )
        mb.action( "aExpandAbbreviation", self.tr( "Expand Abbreviation" ), QIcon( ":/edit/icons/edit/abbreviation.png" ), self.tr( "Ctrl+E" ), self.tr( "Expand Abbreviation" ) ).setEnabled( False )
        mb.action( "aPrepareAPIs", self.tr( "Prepare APIs" ), QIcon( ":/edit/icons/edit/prepareapis.png" ), self.tr( "Ctrl+Alt+P" ), self.tr( "Prepare the APIs files for auto completion / calltips" ) )
        """
        mb.endGroup()
        """TODO
        mb.menu( "mView", self.tr( "View" ) )
        
        mb.beginGroup( "mView" )
        mb.menu( "mStyle", self.tr( "&Style" ), QIcon( ":/view/icons/view/style.png" ) )
        mb.action( "aNext", self.tr( "&Next Tab" ), QIcon( ":/view/icons/view/next.png" ), self.tr( "Ctrl+Tab" ), self.tr( "Active the next tab" ) ).setEnabled( False )
        mb.action( "aPrevious", self.tr( "&Previous Tab" ), QIcon( ":/view/icons/view/previous.png" ), self.tr( "Ctrl+Shift+Tab" ), self.tr( "Active the previous tab" ) ).setEnabled( False )
        mb.action( "aFocusToEditor", self.tr( "Focus Editor" ), QIcon( ":/edit/icons/edit/text.png" ), self.tr( "Ctrl+Return" ), self.tr( "Set the focus to the current document editor" ) )
        mb.endGroup()
        
        mb.menu( "mProject", self.tr( "Project" ) )
        mb.beginGroup( "mProject" )
        
        mb.addAction( '', mks.monkeycore.projectsManager().action( XUPProjectManager.atNew ) )
        mb.addAction( '', mks.monkeycore.projectsManager().action( XUPProjectManager.atOpen ) )
        mb.action( "aSeparator1" )
        mb.addAction( '', mks.monkeycore.projectsManager().action( XUPProjectManager.atClose ) )
        mb.addAction( '', mks.monkeycore.projectsManager().action( XUPProjectManager.atCloseAll ) )
        mb.action( "aSeparator2" )
        mb.addAction( '', mks.monkeycore.projectsManager().action( XUPProjectManager.atEdit ) )
        mb.action( "aSeparator3" )
        mb.addAction( '', mks.monkeycore.projectsManager().action( XUPProjectManager.atAddFiles ) )
        mb.addAction( '', mks.monkeycore.projectsManager().action( XUPProjectManager.atRemoveFiles ) )
        mb.action( "aSeparator4" )
        
        mb.menu( "mRecents", self.tr( "&Recents" ), QIcon( ":/project/icons/project/recents.png" ) )
        mb.action( "mRecents/aClear", self.tr( "&Clear" ), QIcon( ":/project/icons/project/clear.png" ), '', self.tr( "Clear the recents projects list" ) )
        mb.action( "mRecents/aSeparator1" )
        mb.endGroup()
        
        mb.menu( "mBuilder", self.tr( "Build" ) ).menuAction().setEnabled( False )
        mb.menu( "mBuilder" ).menuAction().setVisible( False )
        
        mb.beginGroup( "mBuilder" )
        mb.menu( "mBuild", self.tr( "&Build" ), QIcon( ":/build/icons/build/build.png" ) )
        mb.menu( "mRebuild", self.tr( "&Rebuild" ), QIcon( ":/build/icons/build/rebuild.png" ) )
        mb.menu( "mClean", self.tr( "&Clean" ), QIcon( ":/build/icons/build/clean.png" ) )
        mb.menu( "mExecute", self.tr( "&Execute" ), QIcon( ":/build/icons/build/execute.png" ) )
        mb.menu( "mUserCommands", self.tr( "&User Commands" ), QIcon( ":/build/icons/build/misc.png" ) )
        mb.action( "aSeparator1" )
        mb.endGroup()
        
        mb.menu( "mDebugger", self.tr( "Debugger" ) ).menuAction().setEnabled( False )
        mb.menu( "mDebugger" ).menuAction().setVisible( False )
        mb.menu( "mInterpreter", self.tr( "Interpreter" ) ).menuAction().setEnabled( False )
        mb.menu( "mInterpreter" ).menuAction().setVisible( False )
        mb.menu( "mPlugins", self.tr( "Plugins" ) )
        
        mb.beginGroup( "mPlugins" )
        mb.action( "aSeparator1" )
        mb.endGroup()
        
        mb.menu( "mWindow", self.tr( "Window" ) )

        mb.beginGroup( "mWindow" )
        mb.action( "aCascase", self.tr( "&Cascade" ), QIcon( "" ), '', self.tr( "Cascade" ) )
        mb.action( "aTile", self.tr( "&Tile" ), QIcon( "" ), '', self.tr( "Tile" ) )
        mb.action( "aMinimize", self.tr( "&Minimize" ), QIcon( "" ), '', self.tr( "Minimize" ) )
        mb.action( "aRestore", self.tr( "&Restore" ), QIcon( "" ), '', self.tr( "Restore normal size" ) )
        mb.endGroup()
        mb.menu( "mDocks", self.tr( "Docks" ) )
        """
        mb.menu( "mHelp", self.tr( "Help" ) )

        mb.beginGroup( "mHelp" )
        """TODO
        mb.action( "aAbout", self.tr( "&About..." ), QIcon( ":/application/icons/application/monkey2.png" ), '', self.tr( "About application..." ) )
        """
        mb.action( "aAboutQt", self.tr( "About &Qt..." ), QIcon( ":/help/icons/help/qt.png" ), '', self.tr( "About Qt..." ) )
        mb.action( "aSeparator1" )
        mb.endGroup()
        
        """TODO
        # create action for styles
        agStyles = pStylesActionGroup( self.tr( "Use %1 style" ), mb.menu( "mView/mStyle" ) )
        agStyles.setCurrentStyle( mks.monkeycore.settings().value( "MainWindow/Style" ).toString() )
        mb.menu( "mView/mStyle" ).addActions( agStyles.actions() )
        
        # create plugins actions
        mks.monkeycore.pluginsManager().menuHandler().setMenu( mb.menu( "mPlugins" ) )
        """
    
    def dragEnterEvent( self, event ):
        # if correct mime and same tabbar
        if  event.mimeData().hasUrls() :
            # accept drag
            event.acceptProposedAction()
        
        # default event
        pMainWindow.dragEnterEvent( self, event )
    
    def dropEvent( self, event ):
        if  event.mimeData().hasUrls() :
            self.urlsDropped.emit( event.mimeData().urls () )
        
        # default event
        pMainWindow.dropEvent( self, event )
    
    
    def closeEvent( self, event ):
        """TODO
        # inform that we close mainwindow
        self.aboutToClose.emit()
        
        # save session if needed
        if  mks.monkeystudio.saveSessionOnClose() :
            mks.monkeycore.workspace().fileSessionSave_triggered()
        
        # request close all documents
        if  not mks.monkeycore.workspace().closeAllDocuments() :
            event.ignore()
            return
        
        
        # force to close all projects
        mks.monkeycore.projectsManager().action( XUPProjectManager.atCloseAll ).trigger()
        """
        pMainWindow.closeEvent( self, event )
    
    
    def createPopupMenu(self):
        # create default menu
        menu = QMenu( self );
        # add exclusive action of pDockToolBar
        tbs = self.findChildren(pDockToolBar)
        
        for tb in tbs:
            if  tb.parent() != self :
                continue
            
            menu.addAction( tb.toggleExclusiveAction() )
        
        return menu

    def initToolBar(self):
        # recents
        self.dockToolBar( Qt.TopToolBarArea ).addAction( self.menuBar().menu( "mFile/mRecents" ).menuAction() )
        self.dockToolBar( Qt.TopToolBarArea ).addAction( self.menuBar().menu( "mFile/mSession" ).menuAction() )
        self.dockToolBar( Qt.TopToolBarArea ).addAction( self.menuBar().menu( "mProject/mRecents" ).menuAction() )
        self.dockToolBar( Qt.TopToolBarArea ).addAction()
        # settings
        self.dockToolBar( Qt.TopToolBarArea ).addAction( self.menuBar().action( "mEdit/aSettings" ) )
        self.dockToolBar( Qt.TopToolBarArea ).addAction( self.menuBar().action( "mEdit/aShortcutsEditor" ) )
        # file action
        self.dockToolBar( Qt.TopToolBarArea ).addAction( self.menuBar().action( "mFile/aNew" ) )
        self.dockToolBar( Qt.TopToolBarArea ).addAction( self.menuBar().action( "mFile/aNewTextEditor" ) )
        self.dockToolBar( Qt.TopToolBarArea ).addAction( self.menuBar().action( "mFile/aOpen" ) )
        self.dockToolBar( Qt.TopToolBarArea ).addActions( self.menuBar().menu( "mFile/mSave" ).actions() )
        self.dockToolBar( Qt.TopToolBarArea ).addActions( self.menuBar().menu( "mFile/mClose" ).actions() )
        self.dockToolBar( Qt.TopToolBarArea ).addAction( self.menuBar().action( "mFile/aQuickPrint" ) )
        self.dockToolBar( Qt.TopToolBarArea ).addAction()
        # edit action
        self.dockToolBar( Qt.TopToolBarArea ).addAction( self.menuBar().action( "mEdit/aUndo" ) )
        self.dockToolBar( Qt.TopToolBarArea ).addAction( self.menuBar().action( "mEdit/aRedo" ) )
        self.dockToolBar( Qt.TopToolBarArea ).addAction()
        self.dockToolBar( Qt.TopToolBarArea ).addAction( self.menuBar().action( "mEdit/aCut" ) )
        self.dockToolBar( Qt.TopToolBarArea ).addAction( self.menuBar().action( "mEdit/aCopy" ) )
        self.dockToolBar( Qt.TopToolBarArea ).addAction( self.menuBar().action( "mEdit/aPaste" ) )
        self.dockToolBar( Qt.TopToolBarArea ).addAction()
        self.dockToolBar( Qt.TopToolBarArea ).addAction( self.menuBar().action( "mEdit/aGoTo" ) )
        self.dockToolBar( Qt.TopToolBarArea ).addAction()
        # help action
        self.dockToolBar( Qt.TopToolBarArea ).addAction( self.menuBar().action( "mHelp/aAbout" ) )
        self.dockToolBar( Qt.TopToolBarArea ).addAction()
        # console action
        self.dockToolBar( Qt.TopToolBarArea ).addAction( mks.monkeycore.consoleManager().stopAction() )


    def initConnections(self):
        """TODO
        self.menuBar().action( "mFile/aNew" ).triggered.connect(mks.monkeycore.workspace().fileNew_triggered)
        self.menuBar().action( "mFile/aNewTextEditor" ).triggered.connect(mks.monkeycore.workspace().createNewTextEditor)
        """
        self.menuBar().action( "mFile/aOpen" ).triggered.connect(mks.monkeycore.workspace().fileOpen_triggered)
        """TODO
        mks.monkeycore.recentsManager().openFileRequested.connect(mks.monkeycore.fileManager().openFile)
        self.menuBar().action( "mFile/mSession/aSave" ).triggered.connect(mks.monkeycore.workspace().fileSessionSave_triggered)
        self.menuBar().action( "mFile/mSession/aRestore" ).triggered.connect(mks.monkeycore.workspace().fileSessionRestore_triggered)
        self.menuBar().action( "mFile/mSave/aCurrent" ).triggered.connect(mks.monkeycore.workspace().fileSaveCurrent_triggered)
        self.menuBar().action( "mFile/mSave/aAll" ).triggered.connect(mks.monkeycore.workspace().fileSaveAll_triggered)
        self.menuBar().action( "mFile/mClose/aCurrent" ).triggered.connect(mks.monkeycore.workspace().fileCloseCurrent_triggered)
        self.menuBar().action( "mFile/mClose/aAll" ).triggered.connect(mks.monkeycore.workspace().fileCloseAll_triggered)
        self.menuBar().action( "mFile/aReload" ).triggered.connect(mks.monkeycore.workspace().fileReload_triggered)
        self.menuBar().action( "mFile/aSaveAsBackup" ).triggered.connect(mks.monkeycore.workspace().fileSaveAsBackup_triggered)
        self.menuBar().action( "mFile/aQuickPrint" ).triggered.connect(mks.monkeycore.workspace().fileQuickPrint_triggered)
        self.menuBar().action( "mFile/aPrint" ).triggered.connect(mks.monkeycore.workspace().filePrint_triggered)
        self.menuBar().action( "mFile/aQuit" ).triggered.connect(mks.monkeycore.workspace().fileExit_triggered)
        # edit connection
        self.menuBar().action( "mEdit/aSettings" ).triggered.connect(mks.monkeycore.workspace().editSettings_triggered)
        self.menuBar().action( "mEdit/aShortcutsEditor" ).triggered.connect(mks.monkeycore.actionsManager().editActionsShortcuts)
        self.menuBar().action( "mEdit/aTranslations" ).triggered.connect(mks.monkeycore.workspace().editTranslations_triggered)
        self.menuBar().action( "mEdit/aUndo" ).triggered.connect(mks.monkeycore.workspace().editUndo_triggered)
        self.menuBar().action( "mEdit/aRedo" ).triggered.connect(mks.monkeycore.workspace().editRedo_triggered)
        self.menuBar().action( "mEdit/aCut" ).triggered.connect(mks.monkeycore.workspace().editCut_triggered)
        self.menuBar().action( "mEdit/aCopy" ).triggered.connect(mks.monkeycore.workspace().editCopy_triggered)
        self.menuBar().action( "mEdit/aPaste" ).triggered.connect(mks.monkeycore.workspace().editPaste_triggered)
        self.menuBar().action( "mEdit/mSearchReplace/aSearchFile" ).triggered.connect(mks.monkeycore.workspace().editSearch_triggered)
        #menuBar().action( "mEdit/aSearchPrevious" ).triggered.connect(mks.monkeycore.workspace().editSearchPrevious_triggered)
        #menuBar().action( "mEdit/aSearchNext" ).triggered.connect(mks.monkeycore.workspace().editSearchNext_triggered)
        self.menuBar().action( "mEdit/aGoTo" ).triggered.connect(mks.monkeycore.workspace().editGoTo_triggered)
        self.menuBar().action( "mEdit/aExpandAbbreviation" ).triggered.connect(mks.monkeycore.workspace().editExpandAbbreviation_triggered)
        self.menuBar().action( "mEdit/aPrepareAPIs" ).triggered.connect(mks.monkeycore.workspace().editPrepareAPIs_triggered)
        # view connection
        agStyles.styleSelected.connect(self.changeStyle)
        self.menuBar().action( "mView/aNext" ).triggered.connect(mks.monkeycore.workspace().activateNextDocument)
        self.menuBar().action( "mView/aPrevious" ).triggered.connect(mks.monkeycore.workspace().activatePreviousDocument)
        self.menuBar().action( "mView/aFocusToEditor" ).triggered.connect(mks.monkeycore.workspace().focusEditor)
        # docks
        self.menuBar().menu( "mDocks" ).aboutToShow.connect(self.menu_Docks_aboutToShow)
        # project connection
        mks.monkeycore.recentsManager().openProjectRequested.connect(mks.monkeycore.projectsManager().openProject)
        mks.monkeycore.projectsManager().fileDoubleClicked.connect(mks.monkeycore.workspace().openFile)
        # builder debugger interpreter menu
        self.menuBar().menu( "mBuilder" ).aboutToShow.connect(self.menu_CustomAction_aboutToShow)
        self.menuBar().menu( "mDebugger" ).aboutToShow.connect(self.menu_CustomAction_aboutToShow)
        self.menuBar().menu( "mInterpreter" ).aboutToShow.connect(self.menu_CustomAction_aboutToShow)
        # plugins menu
        # window menu
        self.menuBar().action( "mWindow/aTile" ).triggered.connect(mks.monkeycore.workspace().tile)
        self.menuBar().action( "mWindow/aCascase" ).triggered.connect(mks.monkeycore.workspace().cascade)
        self.menuBar().action( "mWindow/aMinimize" ).triggered.connect(mks.monkeycore.workspace().minimize)
        self.menuBar().action( "mWindow/aRestore" ).triggered.connect(mks.monkeycore.workspace().restore)
        # help menu
        self.menuBar().action( "mHelp/aAbout" ).triggered.connect(mks.monkeycore.workspace().helpAboutApplication_triggered)
        """
        self.menuBar().action( "mHelp/aAboutQt" ).triggered.connect(mks.monkeycore.workspace().helpAboutQt_triggered)
    
    def finalyzeGuiInit(self):
        self.setWindowTitle( "%s v%s (%s)" % (mks.config.PACKAGE_NAME, mks.config.PACKAGE_VERSION, mks.config.PACKAGE_VERSION_STR ) )
        self.setWindowIcon( self.menuBar().action( "mHelp/aAbout" ).icon() )
    
    def menu_Docks_aboutToShow(self):
        # get menu
        menu = self.menuBar().menu( "mDocks" )
        menu.clear()
        
        # add actions
        for dw in self.findChildren(QDockWidget):
            action = dw.toggleViewAction()
            
            action.setIcon( dw.windowIcon() )
            menu.addAction( action )
            self.menuBar().addAction( "mDocks", action )

    def updateMenuVisibility( self, menu ):
        menuAction = menu.menuAction()
        
        menuVisible = False

        for action in menu.actions():
            if  action.isSeparator() :
                continue
            
            subMenu = action.menu()

            if  subMenu :
                if  self.updateMenuVisibility( subMenu ) :
                    menuVisible = True
            else:
                menuVisible = True
        
        menuAction.setVisible( menuVisible )
        menuAction.setEnabled( menuVisible )
        
        return menuVisible
    
    def menu_CustomAction_aboutToShow(self):
        menus = []

        if  sender() :
            menus.append(sender())
        else:
            menus.append[self.menuBar().menu( "mBuilder" )]
            menus.append[self.menuBar().menu( "mDebugger")]
            menus.append[self.menuBar().menu( "mInterpreter")]

        for m in menus:
            self.updateMenuVisibility( m )
    
    def changeStyle( style ):
        qApp.setStyle( style )
        qApp.setPalette( qApp.style().standardPalette() )
        self.settings().setValue( "MainWindow/Style", style )
