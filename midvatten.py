# -*- coding: utf-8 -*-
"""
/***************************************************************************
 This is the main part of the Midvatten plugin. 
 Mainly controlling user interaction and calling for other classes. 
                             -------------------
        begin                : 2011-10-18
        copyright            : (C) 2011 by joskal
        email                : groundwatergis [at] gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import qgis.utils
import resources  # Initialize Qt resources from file resources.py
import os.path # Just to be able to read from metadata.txt in the same directory
from midvsettings import midvsettings
from tsplot import TimeSeriesPlot
from stratigraphy import Stratigraphy
from xyplot import XYPlot
from wqualreport import wqualreport
from loaddefaultlayers import loadlayers
import midvatten_utils as utils         # Whenever some global midvatten_utilities are needed
from definitions import midvatten_defs
#from about.AboutDialog import AboutDialog
from HtmlDialog import HtmlDialog
import sys

#sys.path.append(os.path.dirname(os.path.abspath(__file__))) # To enable loading of modules from inside the plugin directory

class midvatten:
    def __init__(self, iface): # Might need revision of variables and method for loading default variables
        sys.path.append(os.path.dirname(os.path.abspath(__file__))) #add midvatten plugin directory to pythonpath
        self.iface = iface
        # settings...
        self.readingSettings = False # To enable resetsettings
        self.settingsdict = self.createsettingsdict()# calling for the method that defines an empty dictionary of settings NOTE!! byte strings in dict
        #self.loadSettings()    # stored settings are loaded  NOTE: From ver 0.3.2 it is no longer possible to load settings here
        #The settings are stored in the qgis project file and thus cannot be loaded when qgis is starting (and plugin initialized) 
        #The settings are loaded each time a new qgis project is loaded (and several methods below do check that settings really are loaded)
        self.settingsareloaded = False # To make sure settings are loaded once and only once
        
    def initGui(self): # Creates actions that will start plugin configuration
        self.actionNewDB = QAction(QIcon(":/plugins/midvatten/icons/create_new.xpm"), "Create a new Midvatten project DB", self.iface.mainWindow())
        QObject.connect(self.actionNewDB, SIGNAL("triggered()"), self.NewDB)
        
        self.actionloadthelayers = QAction(QIcon(":/plugins/midvatten/icons/loaddefaultlayers.png"), "Load default db-layers to qgis", self.iface.mainWindow())
        self.actionloadthelayers.setWhatsThis("Load default layers from the selected database")
        self.iface.registerMainWindowAction(self.actionloadthelayers, "F7")   # The function should also be triggered by the F7 key
        QObject.connect(self.actionloadthelayers, SIGNAL("activated()"), self.loadthelayers)

        self.actionsetup = QAction(QIcon(":/plugins/midvatten/icons/MidvSettings.png"), "Midvatten Settings", self.iface.mainWindow())
        self.actionsetup.setWhatsThis("Configuration for Midvatten toolset")
        self.iface.registerMainWindowAction(self.actionsetup, "F6")   # The function should also be triggered by the F6 key
        QObject.connect(self.actionsetup, SIGNAL("activated()"), self.setup)
        
        self.actionresetSettings = QAction(QIcon(":/plugins/midvatten/icons/ResetSettings.png"), "Reset Settings", self.iface.mainWindow())
        QObject.connect(self.actionresetSettings, SIGNAL("triggered()"), self.resetSettings)
        
        self.actionabout = QAction(QIcon(":/plugins/midvatten/icons/about.png"), "About", self.iface.mainWindow())
        QObject.connect(self.actionabout, SIGNAL("triggered()"), self.about)
        
        self.actionupdatecoord = QAction(QIcon(":/plugins/midvatten/icons/updatecoordfrpos.png"), "Update coordinates from map position", self.iface.mainWindow())
        QObject.connect(self.actionupdatecoord , SIGNAL("triggered()"), self.updatecoord)
        
        self.actionupdateposition = QAction(QIcon(":/plugins/midvatten/icons/updateposfrcoord.png"), "Update map position from coordinates", self.iface.mainWindow())
        QObject.connect(self.actionupdateposition , SIGNAL("triggered()"), self.updateposition)
        
        self.action_import_wlvl = QAction(QIcon(":/plugins/midvatten/icons/load_wlevels_manual.png"), "Import w level measurements", self.iface.mainWindow())
        QObject.connect(self.action_import_wlvl , SIGNAL("triggered()"), self.import_wlvl)
        
        self.action_import_wflow = QAction(QIcon(":/plugins/midvatten/icons/load_wflow.png"), "Import w flow measurements", self.iface.mainWindow())
        QObject.connect(self.action_import_wflow , SIGNAL("triggered()"), self.import_wflow)
        
        self.action_import_seismics = QAction(QIcon(":/plugins/midvatten/icons/load_seismics.png"), "Import seismic data", self.iface.mainWindow())
        QObject.connect(self.action_import_seismics , SIGNAL("triggered()"), self.import_seismics)
        
        self.action_import_vlf = QAction(QIcon(":/plugins/midvatten/icons/load_vlf.png"), "Import vlf data", self.iface.mainWindow())
        QObject.connect(self.action_import_vlf , SIGNAL("triggered()"), self.import_vlf)
        
        self.action_import_obs_lines = QAction(QIcon(":/plugins/midvatten/icons/import_obs_lines.png"), "Import obs lines table", self.iface.mainWindow())
        QObject.connect(self.action_import_obs_lines , SIGNAL("triggered()"), self.import_obs_lines)
        
        self.action_wlvlcalculate = QAction(QIcon(":/plugins/midvatten/icons/calc_level_masl.png"), "Calculate w level above sea level", self.iface.mainWindow())
        QObject.connect(self.action_wlvlcalculate , SIGNAL("triggered()"), self.wlvlcalculate)
        
        self.action_import_wlvllogg = QAction(QIcon(":/plugins/midvatten/icons/load_wlevels_logger.png"), "Import w level from logger", self.iface.mainWindow())
        QObject.connect(self.action_import_wlvllogg , SIGNAL("triggered()"), self.import_wlvllogg)
        
        self.action_wlvlloggcalibrate = QAction(QIcon(":/plugins/midvatten/icons/calibr_level_logger_masl.png"), "Calibrate w level from logger", self.iface.mainWindow())
        QObject.connect(self.action_wlvlloggcalibrate , SIGNAL("triggered()"), self.wlvlloggcalibrate)

        self.actionimport_wqual_lab = QAction(QIcon(":/plugins/midvatten/icons/import_wqual_lab.png"), "Import w quality from lab", self.iface.mainWindow())
        QObject.connect(self.actionimport_wqual_lab, SIGNAL("triggered()"), self.import_wqual_lab)
        
        self.actionimport_wqual_field = QAction(QIcon(":/plugins/midvatten/icons/import_wqual_field.png"), "Import w quality from field", self.iface.mainWindow())
        QObject.connect(self.actionimport_wqual_field, SIGNAL("triggered()"), self.import_wqual_field)
        
        self.actionimport_stratigraphy = QAction(QIcon(":/plugins/midvatten/icons/import_stratigraphy.png"), "Import stratigraphy data", self.iface.mainWindow())
        QObject.connect(self.actionimport_stratigraphy, SIGNAL("triggered()"), self.import_stratigraphy)
        
        self.actionimport_obs_points = QAction(QIcon(":/plugins/midvatten/icons/import_obs_points.png"), "Import obs points table", self.iface.mainWindow())
        QObject.connect(self.actionimport_obs_points, SIGNAL("triggered()"), self.import_obs_points)
        
        self.actionimport_wflow = QAction(QIcon(":/plugins/midvatten/icons/import_wflow.png"), "Import w flow measurements", self.iface.mainWindow())
        QObject.connect(self.actionimport_wflow, SIGNAL("triggered()"), self.import_wflow)
        
        self.actionPlotTS = QAction(QIcon(":/plugins/midvatten/icons/PlotTS.png"), "Time series plot", self.iface.mainWindow())
        self.actionPlotTS.setWhatsThis("Plot time series for selected objects")
        self.iface.registerMainWindowAction(self.actionPlotTS, "F8")   # The function should also be triggered by the F8 key
        QObject.connect(self.actionPlotTS, SIGNAL("triggered()"), self.PlotTS)
        
        self.actionPlotXY = QAction(QIcon(":/plugins/midvatten/icons/PlotXY.png"), "Scatter plot", self.iface.mainWindow())
        self.actionPlotXY.setWhatsThis("Plot XY scatter data (e.g. seismic profiel) for the selected objects")
        self.iface.registerMainWindowAction(self.actionPlotXY, "F9")   # The function should also be triggered by the F9 key
        QObject.connect(self.actionPlotXY, SIGNAL("triggered()"), self.PlotXY)
        
        self.actionPlotStratigraphy = QAction(QIcon(":/plugins/midvatten/icons/PlotStratigraphy.png"), "Plot stratigraphy", self.iface.mainWindow())
        self.actionPlotStratigraphy.setWhatsThis("Show stratigraphy for selected objects (modified ARPAT)")
        self.iface.registerMainWindowAction(self.actionPlotStratigraphy, "F10")   # The function should also be triggered by the F10 key
        QObject.connect(self.actionPlotStratigraphy, SIGNAL("triggered()"), self.PlotStratigraphy)
        
        self.actiondrillreport = QAction(QIcon(":/plugins/midvatten/icons/drill_report.png"), "General Report", self.iface.mainWindow())
        self.actiondrillreport.setWhatsThis("Show a general report for the selected obs point")
        self.iface.registerMainWindowAction(self.actiondrillreport, "F11")   # The function should also be triggered by the F11 key
        QObject.connect(self.actiondrillreport, SIGNAL("triggered()"), self.drillreport)

        self.actionwqualreport = QAction(QIcon(":/plugins/midvatten/icons/wqualreport.png"), "Water Quality Report", self.iface.mainWindow())
        self.actionwqualreport.setWhatsThis("Show water quality for the selected obs point")
        self.iface.registerMainWindowAction(self.actionwqualreport, "F12")   # The function should also be triggered by the F12 key
        QObject.connect(self.actionwqualreport, SIGNAL("triggered()"), self.waterqualityreport)

        self.actionChartMaker = QAction(QIcon(":/plugins/midvatten/icons/ChartMakerSQLite.png"), "ChartMaker for Midvatten DB", self.iface.mainWindow())
        self.actionChartMaker.setWhatsThis("Start ChartMaker for SQLite data")
        #self.iface.registerMainWindowAction(self.actionChartMaker, "F12")   # The function should also be triggered by the F12 key
        QObject.connect(self.actionChartMaker, SIGNAL("triggered()"), self.ChartMaker)

        # Add toolbar with buttons 
        self.toolBar = self.iface.addToolBar("Midvatten")
        self.toolBar.addAction(self.actionsetup)
        #self.toolBar.addAction(self.actionloadthelayers)
        self.toolBar.addAction(self.actionPlotTS)
        self.toolBar.addAction(self.actionPlotXY)
        self.toolBar.addAction(self.actionPlotStratigraphy)
        self.toolBar.addAction(self.actiondrillreport)
        self.toolBar.addAction(self.actionwqualreport)
        #self.toolBar.addAction(self.actionChartMaker)
        
        # Add plugins menu items
        self.menu = QMenu("Midvatten")
        self.menu.import_data_menu = QMenu(QCoreApplication.translate("Midvatten", "&Import data to database"))
        #self.iface.addPluginToMenu("&Midvatten", self.menu.add_data_menu.menuAction())
        self.menu.addMenu(self.menu.import_data_menu)
        self.menu.import_data_menu.addAction(self.actionimport_obs_points)   
        self.menu.import_data_menu.addAction(self.action_import_wlvl)   
        self.menu.import_data_menu.addAction(self.action_import_wlvllogg)   
        self.menu.import_data_menu.addAction(self.actionimport_wqual_lab)
        self.menu.import_data_menu.addAction(self.actionimport_wqual_field)   
        self.menu.import_data_menu.addAction(self.action_import_wflow)   
        self.menu.import_data_menu.addAction(self.actionimport_stratigraphy)   
        self.menu.import_data_menu.addAction(self.action_import_obs_lines)   
        self.menu.import_data_menu.addAction(self.action_import_seismics)   
        self.menu.import_data_menu.addAction(self.action_import_vlf)   

        self.menu.add_data_menu = QMenu(QCoreApplication.translate("Midvatten", "&Edit data in database"))
        #self.iface.addPluginToMenu("&Midvatten", self.menu.add_data_menu.menuAction())
        self.menu.addMenu(self.menu.add_data_menu)
        self.menu.add_data_menu.addAction(self.action_wlvlcalculate)   
        self.menu.add_data_menu.addAction(self.action_wlvlloggcalibrate)   
        self.menu.add_data_menu.addAction(self.actionupdatecoord)   
        self.menu.add_data_menu.addAction(self.actionupdateposition)   

        self.menu.plot_data_menu = QMenu(QCoreApplication.translate("Midvatten", "&View plot"))
        #self.iface.addPluginToMenu("&Midvatten", self.menu.plot_data_menu.menuAction())
        self.menu.addMenu(self.menu.plot_data_menu)
        self.menu.plot_data_menu.addAction(self.actionPlotTS) 
        self.menu.plot_data_menu.addAction(self.actionPlotXY)
        self.menu.plot_data_menu.addAction(self.actionPlotStratigraphy)
        #self.menu.plot_data_menu.addAction(self.actionChartMaker)          #Not until implemented!

        self.menu.report_menu = QMenu(QCoreApplication.translate("Midvatten", "&View report"))
        self.menu.addMenu(self.menu.report_menu)
        self.menu.report_menu.addAction(self.actiondrillreport)
        self.menu.report_menu.addAction(self.actionwqualreport)

        self.menu.addSeparator()
        self.menu.addAction(self.actionNewDB)
        self.menu.addAction(self.actionloadthelayers)   
        self.menu.addAction(self.actionsetup)
        self.menu.addAction(self.actionresetSettings)
        self.menu.addAction(self.actionabout)
        #self.iface.addPluginToMenu("&Midvatten", self.actionsetup)
        #self.iface.addPluginToMenu("&Midvatten", self.actionresetSettings)
        #self.iface.addPluginToMenu("&Midvatten", self.actionabout)
        menuBar = self.iface.mainWindow().menuBar()
        menuBar.addMenu(self.menu)

        # QGIS iface connections
        self.iface.projectRead.connect(self.loadSettings)
        self.iface.newProjectCreated.connect(self.resetSettings)
        
    def unload(self):    
        # Remove the plugin menu items and icons
        self.menu.deleteLater()
        #self.iface.removePluginMenu("&Midvatten", self.add_data_menu.menuAction())
        #self.iface.removePluginMenu("&Midvatten", self.plot_data_menu.menuAction())
        #self.iface.removePluginMenu("&Midvatten", self.actionsetup)
        #self.iface.removePluginMenu("&Midvatten", self.actionresetSettings)
        #self.iface.removePluginMenu("&Midvatten", self.actionabout)
        
        # remove tool bar
        del self.toolBar
        
        # Also remove F5 - F12 key triggers
        self.iface.unregisterMainWindowAction(self.actionloadthelayers)
        self.iface.unregisterMainWindowAction(self.actionsetup)
        self.iface.unregisterMainWindowAction(self.actionPlotTS)
        self.iface.unregisterMainWindowAction(self.actionPlotXY)
        self.iface.unregisterMainWindowAction(self.actionPlotStratigraphy)
        self.iface.unregisterMainWindowAction(self.actiondrillreport)
        self.iface.unregisterMainWindowAction(self.actionwqualreport)
        self.iface.unregisterMainWindowAction(self.actionChartMaker)
        sys.path.remove(os.path.dirname(os.path.abspath(__file__))) #Clean up python environment

    def about(self):   
        #filenamepath = os.path.dirname(__file__) + "/metadata.txt"
        filenamepath = os.path.join(os.path.dirname(__file__),"metadata.txt" )
        iniText = QSettings(filenamepath , QSettings.IniFormat)#This method seems to return a list of unicode strings BUT it seems as if the encoding from the byte strings in the file is not utf-8, hence there is need for special encoding, see below
        verno = str(iniText.value('version'))
        author = iniText.value('author').encode('cp1252')#.encode due to encoding probs
        email = str(iniText.value('email'))
        homepage = str(iniText.value('homepage'))

        ABOUT_templatefile = os.path.join(os.sep,os.path.dirname(__file__),"about","about_template.htm")
        ABOUT_outputfile = os.path.join(os.sep,os.path.dirname(__file__),"about","about.htm")
        f_in = open(ABOUT_templatefile, 'r')
        f_out = open(ABOUT_outputfile, 'w')
        wholefile = f_in.read()
        changedfile = wholefile.replace('VERSIONCHANGETHIS',verno).replace('AUTHORCHANGETHIS',author).replace('EMAILCHANGETHIS',email).replace('HOMEPAGECHANGETHIS',homepage)
        f_out.write(changedfile)
        f_in.close()
        f_out.close()
        #infoString = QString("This is the Midvatten toolset for QGIS. ")
        #infoString = infoString.append(QString("\n<a href=\'" + homepage + "'></a>"))
        #infoString = infoString.append("\n\n" + verno)
        #infoString = infoString.append("\nAuthor: " + author)
        #infoString = infoString.append("\nEmail: " + email)
        #QMessageBox.information(self.iface.mainWindow(), "About the Midvatten toolset", infoString)
        dlg = HtmlDialog("About Midvatten plugin for QGIS",QUrl.fromLocalFile(ABOUT_outputfile))
        dlg.exec_()

    def ChartMaker(self): #  - Not ready - 
        if self.settingsareloaded == False:    # If this is the first thing the user does, then load settings from project file
            self.loadSettings()    
        utils.pop_up_info("not yet implemented") #for debugging

    def createsettingsdict(self):# Here is where an empty settings dictionary is defined, NOTE! byte strings in dictionary
        dictionary = midvatten_defs.settingsdict()
        return dictionary

    def drillreport(self):             
        if self.settingsareloaded == False:    # If this is the first thing user does - then load settings from project file
            self.loadSettings()    
        allcritical_layers = ('obs_points', 'w_levels', 'w_qual_lab')     #Check that none of these layers are in editing mode
        for layername in allcritical_layers:    # A warning if some of the layers are in editing mode
            layerexists = utils.find_layer(str(layername))
            if layerexists:
                if layerexists.isEditable():
                    utils.pop_up_info("Layer " + str(layerexists.name()) + " is currently in editing mode.\nPlease consider exiting this mode before generating a report.", "Warning")

        if not (self.settingsdict['database'] == ''):
            if qgis.utils.iface.activeLayer():
                if utils.selection_check(qgis.utils.iface.activeLayer(),1) == 'ok': #only one selected object
                    obsid = utils.getselectedobjectnames()  # selected obs_point is now found in obsid[0]
                    from drillreport import drillreport
                    drillreport(obsid[0],self.settingsdict) 
                else:
                    utils.pop_up_info("You have to select exactly one observation point!","Attention")
            else:
                utils.pop_up_info("You have to select the obs_points layer and the observation point (just one!) for which to generate a general report!", "Attention")
        else: 
            utils.pop_up_info("Check settings! \nYou have to select database first!")
        
    def import_obs_lines(self):
        errorsignal = 0
        if self.settingsareloaded == False:    # If this is the first does - then load settings from project file
            self.loadSettings()    

        allcritical_layers = ('obs_lines')     #Check that none of these layers are in editing mode
        for layername in allcritical_layers:
            layerexists = utils.find_layer(str(layername))
            if layerexists:
                if layerexists.isEditable():
                    utils.pop_up_info("Layer " + str(layerexists.name()) + " is currently in editing mode.\nPlease exit this mode before importing data.", "Warning")
                    errorsignal = 1

        if errorsignal == 0:        # unless none of the critical layers are in editing mode
            sanity = utils.askuser("YesNo","""You are about to import observation lines data, from a text file which must have one header row and 6 columns (see plugin web page for further explanation):\nWKT;obsid;name;place;type;source\n\nPlease note that:\nThere must be WKT geometries of type LINESTRING in the first column.\nThe LINESTRING geometries must correspond to SRID in the dataabse.\nThe file must be either comma, or semicolon-separated.\nDecimal separator must be point (.)\nComma or semicolon is not allowed in string fields.\nEmpty or null values are not allowed for obsid and there must not be any duplicates of obsid\n\nContinue?""",'Are you sure?')
            #utils.pop_up_info(sanity.result)   #debugging
            if sanity.result == 1:
                from import_data_to_db import midv_data_importer
                importinstance = midv_data_importer()
                importinstance.obslines_import()
                if importinstance.status=='True':      #
                    utils.pop_up_info("%s observation lines were imported to the database."%str(importinstance.recsafter - importinstance.recsbefore))
                    #self.iface.messageBar().pushMessage("Info","%s observation lines were imported to the database."%str(importinstance.recsafter - importinstance.recsbefore), 0)
                #else:  
                    #self.iface.messageBar().pushMessage("Warning","Something failed during import", 1)
                    #utils.pop_up_info("Something failed during import") 

    def import_obs_points(self):
        errorsignal = 0
        if self.settingsareloaded == False:    # If this is the first does - then load settings from project file
            self.loadSettings()    

        allcritical_layers = ('obs_points')     #Check that none of these layers are in editing mode
        for layername in allcritical_layers:
            layerexists = utils.find_layer(str(layername))
            if layerexists:
                if layerexists.isEditable():
                    utils.pop_up_info("Layer " + str(layerexists.name()) + " is currently in editing mode.\nPlease exit this mode before importing data.", "Warning")
                    errorsignal = 1

        if errorsignal == 0:        # unless none of the critical layers are in editing mode
            sanity = utils.askuser("YesNo","""You are about to import observation points data, from an ascii text file which must have one header row and 26 columns (see plugin web page for further explanation):\n\n1. obsid, 2. name, 3. place, 4. type, 5. length, 6. drillstop, 7. diam, 8. material, 9. screen, 10. capacity, 11. drilldate, 12. wmeas_yn, 13. wlogg_yn, 14. east, 15. north, 16. ne_accur, 17. ne_source, 18. h_toc, 19. h_tocags, 20. h_gs, 21. h_accur, 22. h_syst, 23. h_source, 24. source, 25. com_onerow, 26. com_html\n\nPlease note that:\nThe file must be either comma, or semicolon-separated.\nDecimal separator must be point (.)\nComma or semicolon is not allowed in string fields.\nEmpty or null values are not allowed for obsid and there must not be any duplicates of obsid.\nEast and north values must correspond to the database SRID.\n\nContinue?""",'Are you sure?')
            #utils.pop_up_info(sanity.result)   #debugging
            if sanity.result == 1:
                from import_data_to_db import midv_data_importer
                importinstance = midv_data_importer()
                importinstance.obsp_import()
                #utils.pop_up_info(returnvalue) #debugging
                #utils.pop_up_info(importinstance.status) #debugging
                if importinstance.status=='True':      # 
                    utils.pop_up_info("%s observation points were imported to the database.\nTo display the imported points on map, select them in\nthe obs_points attribute table then update map position:\nMidvatten - Edit data in database - Update map position from coordinates"%str(importinstance.recsafter - importinstance.recsbefore))
                #else:  
                    #self.iface.messageBar().pushMessage("Warning","Something failed during import", 1)
                    #utils.pop_up_info("Something failed during import") #for debugging

    def import_seismics(self):
        errorsignal = 0
        if self.settingsareloaded == False:    # If this is the first does - then load settings from project file
            self.loadSettings()    
        allcritical_layers = ('obs_lines', 'seismic_data')     #Check that none of these layers are in editing mode
        for layername in allcritical_layers:
            layerexists = utils.find_layer(str(layername))
            if layerexists:
                if layerexists.isEditable():
                    utils.pop_up_info("Layer " + str(layerexists.name()) + " is currently in editing mode.\nPlease exit this mode before importing data.", "Warning")
                    errorsignal = 1

        if errorsignal == 0:        # om ingen av de kritiska lagren är i editeringsmode
            sanity = utils.askuser("YesNo","""You are about to import interpreted seismic data, from a text file which must have one header row and 7 columns:\n\nobsid,length,east,north,ground,bedrock,gw_table\n\nPlease note that:\nThe file must be either comma, or semicolon-separated.\nDecimal separator must be point (.)\nEmpty or null values are not allowed for obsid or length.\nEach combination of obsid and length must be unique.\n\nContinue?""",'Are you sure?')
            #utils.pop_up_info(sanity.result)   #debugging
            if sanity.result == 1:
                from import_data_to_db import midv_data_importer
                importinstance = midv_data_importer()
                importinstance.seismics_import()
                if importinstance.status=='True':      #Why is this if statement? Nothing more is to be done! 
                    self.iface.messageBar().pushMessage("Info","%s interpreted seismic data values were imported to the database"%str(importinstance.recsafter - importinstance.recsbefore), 0)
                #else:  
                #    self.iface.messageBar().pushMessage("Warning","Something failed during import", 1)

    def import_stratigraphy(self):
        errorsignal = 0
        if self.settingsareloaded == False:    # If this is the first does - then load settings from project file
            self.loadSettings()    

        allcritical_layers = ('obs_points', 'stratigraphy')     #Check that none of these layers are in editing mode
        for layername in allcritical_layers:
            layerexists = utils.find_layer(str(layername))
            if layerexists:
                if layerexists.isEditable():
                    utils.pop_up_info("Layer " + str(layerexists.name()) + " is currently in editing mode.\nPlease exit this mode before importing data.", "Warning")
                    errorsignal = 1

        if errorsignal == 0:        # unless none of the critical layers are in editing mode
            sanity = utils.askuser("YesNo","""You are about to import stratigraphy data, from an ascii text file which must have one header row and 9 columns:\n1. obsid\n2. stratid - integer starting from ground surface and increasing downwards\n3. depth_top - depth to top of stratigraphy layer\n4. depth_bot - depth to bottom of stratigraphy layer\n5. geology\n6. geoshort - shortname for layer geology (see dicionary)\n7. capacity\n8. development - well development\n9. comment\n\nPlease note that:\nThe file must be either comma, or semicolon-separated.\ndate_time must be of format 'yyyy-mm-dd hh:mm(:ss)'.\nDecimal separator must be point (.)\nComma or semicolon is not allowed in the comments.\nEmpty or null values are not allowed for obsid or stratid, such rows will be excluded from the import.\nEach combination of obsid and stratid must be unique.\n\nContinue?""",'Are you sure?')
            #utils.pop_up_info(sanity.result)   #debugging
            if sanity.result == 1:
                from import_data_to_db import midv_data_importer
                importinstance = midv_data_importer()
                importinstance.strat_import()
                if importinstance.status=='True':      # 
                    self.iface.messageBar().pushMessage("Info","%s stratigraphy layers were imported to the database"%str(importinstance.recsafter - importinstance.recsbefore), 0)
                #else:  
                #    self.iface.messageBar().pushMessage("Warning","Something failed during import", 1)
                    
    def import_vlf(self):
        errorsignal = 0
        if self.settingsareloaded == False:    # If this is the first does - then load settings from project file
            self.loadSettings()    

        allcritical_layers = ('obs_lines', 'vlf_data')     #Check that none of these layers are in editing mode
        for layername in allcritical_layers:
            layerexists = utils.find_layer(str(layername))
            if layerexists:
                if layerexists.isEditable():
                    utils.pop_up_info("Layer " + str(layerexists.name()) + " is currently in editing mode.\nPlease exit this mode before importing data.", "Warning")
                    errorsignal = 1

        if errorsignal == 0:        # om ingen av de kritiska lagren är i editeringsmode
            sanity = utils.askuser("YesNo","""You are about to import raw data from vlf measurements, from a text file which must have one header row and 6 columns:\n\nobsid;length;east;north;real_comp;imag_comp\n\nPlease note that:\nThe file must be either comma, or semicolon-separated.\nDecimal separator must be point (.)\nEmpty or null values are not allowed for obsid or length.\nEach combination of obsid and length must be unique.\n\nContinue?""",'Are you sure?')
            #utils.pop_up_info(sanity.result)   #debugging
            if sanity.result == 1:
                from import_data_to_db import midv_data_importer
                importinstance = midv_data_importer()
                importinstance.vlf_import()
                if importinstance.status=='True': 
                    self.iface.messageBar().pushMessage("Info","%s raw values of vlf measurements were imported to the database"%str(importinstance.recsafter - importinstance.recsbefore), 0)
                #else:  
                #    self.iface.messageBar().pushMessage("Warning","Something failed during import", 1)

    def import_wflow(self):
        errorsignal = 0
        if self.settingsareloaded == False:    # If this is the first does - then load settings from project file
            self.loadSettings()    

        allcritical_layers = ('obs_points', 'w_flow')     #Check that none of these layers are in editing mode
        for layername in allcritical_layers:
            layerexists = utils.find_layer(str(layername))
            if layerexists:
                if layerexists.isEditable():
                    utils.pop_up_info("Layer " + str(layerexists.name()) + " is currently in editing mode.\nPlease exit this mode before importing data.", "Warning")
                    errorsignal = 1

        if errorsignal == 0:        # om ingen av de kritiska lagren är i editeringsmode
            sanity = utils.askuser("YesNo","""You are about to import water flow reading, from an ascii text file which must have one header row and 7 columns:\n\n1. obsid\n2. instrumentid\n3. flowtype\n4. date_time\n5. reading\n6. unit\n7. comment\n\nPlease note that:\nThe file must be either comma, or semicolon-separated.\ndate_time must be of format 'yyyy-mm-dd hh:mm(:ss)'.\nDecimal separator must be point (.)\nComma or semicolon is not allowed in the comments.\nBe sure to use a limited number of flowtypes since all new flowtypes will silently be added to the database table zz_flowtype during import.\nEmpty or null values are not allowed for obsid, instrumentid, flowtype or date_time.\nEach combination of obsid, instrumentid, flowtype or date_time must be unique.\n\nContinue?""",'Are you sure?')
            #utils.pop_up_info(sanity.result)   #debugging
            if sanity.result == 1:
                from import_data_to_db import midv_data_importer
                importinstance = midv_data_importer()
                importinstance.wflow_import()
                if importinstance.status=='True':      # 
                    self.iface.messageBar().pushMessage("Info","%s water flow readings were imported to the database"%str(importinstance.recsafter - importinstance.recsbefore), 0)
                #else:  
                #    self.iface.messageBar().pushMessage("Warning","Something failed during import", 1)

    def import_wlvl(self):    
        errorsignal = 0
        if self.settingsareloaded == False:    # If this is the first does - then load settings from project file
            self.loadSettings()    

        allcritical_layers = ('obs_points', 'w_levels')     #Check that none of these layers are in editing mode
        for layername in allcritical_layers:
            layerexists = utils.find_layer(str(layername))
            if layerexists:
                if layerexists.isEditable():
                    utils.pop_up_info("Layer " + str(layerexists.name()) + " is currently in editing mode.\nPlease exit this mode before importing data.", "Warning")
                    errorsignal = 1

        if errorsignal == 0:        # om ingen av de kritiska lagren är i editeringsmode
            sanity = utils.askuser("YesNo","""You are about to import water level measurements, from an ascii text file which must have one header row and 4 columns:\n\nobsid;date_time;meas;comment\n\nPlease note that:\nThe file must be either comma, or semicolon-separated.\ndate_time must be of format 'yyyy-mm-dd hh:mm(:ss)'.\nDecimal separator must be point (.)\nComma or semicolon is not allowed in the comments.\nEmpty or null values are not allowed for obsid or date_time, such rows will be excluded from the import.\nEmpty or null values are not accepted at the same time in both the columns meas and comment.\nEach combination of obsid and date_time must be unique.\n\nContinue?""",'Are you sure?')
            #utils.pop_up_info(sanity.result)   #debugging
            if sanity.result == 1:
                from import_data_to_db import midv_data_importer
                importinstance = midv_data_importer()
                importinstance.wlvl_import()
                if importinstance.status=='True': 
                    self.iface.messageBar().pushMessage("Info","%s water level measurements were imported to the database"%str(importinstance.recsafter - importinstance.recsbefore), 0)
                #else:  
                #    self.iface.messageBar().pushMessage("Warning","Something failed during import", 1)
                    
    def import_wlvllogg(self):#  - should be rewritten 
        errorsignal = 0
        if self.settingsareloaded == False:    # If this is the first thing user does - then load settings from project file
            self.loadSettings()    

        allcritical_layers = ('obs_points', 'w_levels_logger')     #Check that none of these layers are in editing mode
        for layername in allcritical_layers:
            layerexists = utils.find_layer(str(layername))
            if layerexists:
                if layerexists.isEditable():
                    utils.pop_up_info("Layer " + str(layerexists.name()) + " is currently in editing mode.\nPlease exit this mode before importing data.", "Warning")
                    errorsignal = 1

        if errorsignal == 0:        # om ingen av de kritiska lagren är i editeringsmode
            if not (self.settingsdict['database'] == ''):
                if qgis.utils.iface.activeLayer():
                    if utils.selection_check(qgis.utils.iface.activeLayer(),1) == 'ok':                
                        obsid = utils.getselectedobjectnames()                    
                        longmessage = """You are about to import water head data, recorded with a\nLevel Logger (e.g. Diver), for """
                        longmessage += obsid[0]
                        longmessage +=u""".\nData is supposed to be imported from a semicolon or comma\nseparated ascii text file. The text file must have one header row and columns:\n\nDate/time,Water head[cm],Temperature[°C]\nor\nDate/time,Water head[cm],Temperature[°C],1:Conductivity[mS/cm]\n\nColumn names are unimportant although column order is.\nAlso, date-time must have format yyyy-mm-dd hh:mm(:ss) and\nthe other columns must be real numbers with point(.) as decimal separator and no separator for thousands.\nRemember to not use comma in the comment field!\n\nAlso, records where any fields are empty will be excluded from the report!\n\nContinue?"""
                        sanity = utils.askuser("YesNo",utils.returnunicode(longmessage),'Are you sure?')
                        if sanity.result == 1:
                            from import_data_to_db import wlvlloggimportclass
                            importinstance = wlvlloggimportclass()
                            if not importinstance.status=='True':      
                                self.iface.messageBar().pushMessage("Warning","Something failed during import", 1)
                else:
                    self.iface.messageBar().pushMessage("Critical","You have to select the obs_points layer and the object (just one!) for which logger data is to be imported!", 2)
            else: 
                self.iface.messageBar().pushMessage("Check settings","You have to select database first!",2)

    def import_wqual_field(self):
        errorsignal = 0
        if self.settingsareloaded == False:    # If this is the first does - then load settings from project file
            self.loadSettings()    

        allcritical_layers = ('obs_points', 'w_qual_field')     #Check that none of these layers are in editing mode
        for layername in allcritical_layers:
            layerexists = utils.find_layer(str(layername))
            if layerexists:
                if layerexists.isEditable():
                    utils.pop_up_info("Layer " + str(layerexists.name()) + " is currently in editing mode.\nPlease exit this mode before importing data.", "Warning")
                    errorsignal = 1

        if errorsignal == 0:        # unless none of the critical layers are in editing mode
            sanity = utils.askuser("YesNo","""You are about to import water quality data from field measurements, from an ascii text file which must have one header row and the following 10 columns:\n\n1. obsid\n2. staff\n3. date_time - on format yyyy-mm-dd hh:mm(:ss)\n4. instrument\n5. parameter - water quality parameter name\n6. reading_num - param. value (real number, decimal separator=point(.))\n7. reading_txt - parameter value as text, including <, > etc\n8. unit\n9. flow_lpm - sampling flow in litres/minute\n10. comment - text string\n\nPlease note that:\nThe file must be either comma, or semicolon-separated.\ndate_time must be of format 'yyyy-mm-dd hh:mm(:ss)'.\nDecimal separator must be point (.)\nComma or semicolon is not allowed in the comments.\nEmpty or null values are not allowed for obsid, date_time or parameter, such rows will be excluded from the import.\nEach combination of obsid, date_time and parameter must be unique.\n\nContinue?""",'Are you sure?')
            #utils.pop_up_info(sanity.result)   #debugging
            if sanity.result == 1:
                from import_data_to_db import midv_data_importer
                importinstance = midv_data_importer()
                importinstance.wqualfield_import()
                if importinstance.status=='True':      # 
                    self.iface.messageBar().pushMessage("Info","%s water quality paramters were imported to the database"%str(importinstance.recsafter - importinstance.recsbefore), 0)
                #else:  
                #    self.iface.messageBar().pushMessage("Warning","Something failed during import", 1)
                    
    def import_wqual_lab(self):
        errorsignal = 0
        if self.settingsareloaded == False:    # If this is the first does - then load settings from project file
            self.loadSettings()    

        allcritical_layers = ('obs_points', 'w_qual_lab')     #Check that none of these layers are in editing mode
        for layername in allcritical_layers:
            layerexists = utils.find_layer(str(layername))
            if layerexists:
                if layerexists.isEditable():
                    utils.pop_up_info("Layer " + str(layerexists.name()) + " is currently in editing mode.\nPlease exit this mode before importing data.", "Warning")
                    errorsignal = 1

        if errorsignal == 0:        # unless none of the critical layers are in editing mode
            sanity = utils.askuser("YesNo","""You are about to import water quality data from laboratory analysis, from an ascii text file which must have one header row and the following 12 columns:\n\n1. obsid - must exist in obs_points table\n2. depth - sample depth (real number)\n3. report - each pair of 'report' & 'parameter' must be unique!\n4. project\n5. staff\n6. date_time - on format yyyy-mm-dd hh:mm(:ss)\n7. analysis_method\n8. parameter - water quality parameter name\n9. reading_num - param. value (real number, decimal separator=point(.))\n10. reading_txt - parameter value as text, including <, > etc\n11. unit\n12. comment - text string, avoid semicolon and commas\n\nPlease note that:\nThe file must be either comma, or semicolon-separated.\ndate_time must be of format 'yyyy-mm-dd hh:mm(:ss)'.\nDecimal separator must be point (.)\nComma or semicolon is not allowed in the comments.\nEmpty or null values are not allowed for obsid, report or parameter, such rows will be excluded from the import.\nEach combination of report and parameter must be unique.\n\nContinue?""",'Are you sure?')
            #utils.pop_up_info(sanity.result)   #debugging
            if sanity.result == 1:
                from import_data_to_db import midv_data_importer
                importinstance = midv_data_importer()
                importinstance.wquallab_import()
                if importinstance.status=='True':      # 
                    self.iface.messageBar().pushMessage("Info","%s water quality parameters were imported to the database"%str(importinstance.recsafter - importinstance.recsbefore), 0)
                #else:  
                #    self.iface.messageBar().pushMessage("Warning","Something failed during import", 1)
            
    def loadSettings(self):# settingsdict is a dictionary belonging to instance midvatten. Must be stored and loaded here.
        """read plugin settings from QgsProject instance"""
        self.settingsdict = self.createsettingsdict()
        self.readingSettings = True  
        # map data types to function names
        prj = QgsProject.instance()
        functions = { 'str' : prj.readEntry,
                     'str' : prj.readEntry, # SIP API UPDATE 2.0
                     'int' : prj.readNumEntry,
                     'float' : prj.readDoubleEntry,
                     'bool' : prj.readBoolEntry,
                     'datetime' : prj.readDoubleEntry, # we converted datetimes to float in writeSetting()
                     'list' : prj.readListEntry, # SIP API UPDATE 2.0
                     'pyqtWrapperType' : prj.readListEntry # strange name for QStringList
                     }
        output = {}
        for (key, value) in self.settingsdict.items():
            dataType = type(value).__name__
            try:
                func = functions[dataType]
                output[key] = func("Midvatten", key)
                self.settingsdict[key] = output[key][0]
            except KeyError:
                self.iface.messageBar().pushMessage("Info","Settings key %s does not exist in project file."%str(key), 0,duration=30)
        self.readingSettings = False
        self.settingsareloaded = True

    def loadthelayers(self):            
        if self.settingsareloaded == False:    # If this is the first thing the user does, then load settings from project file
            self.loadSettings()    
        if not self.settingsdict['database'] == '':
            sanity = utils.askuser("YesNo","""This operation will load default layers ( with predefined layout, edit forms etc.) from your selected database to your qgis project.\n\nIf any default Midvatten DB layers already are loaded into your qgis project, then those layers first will be removed from your qgis project.\n\nProceed?""",'Warning!')
            if sanity.result == 1:
                loadlayers(qgis.utils.iface, self.settingsdict)
                self.iface.mapCanvas().zoomToFullExtent()#zoom to full extent to let user see what was loaded
                #self.iface.mapCanvas().refresh()  # to redraw after loaded symbology
        else:   
            utils.pop_up_info("You have to select a database in Midvatten settings first!")

    def NewDB(self): 
        sanity = utils.askuser("YesNo","""This will create a new empty\nMidvatten DB with predefined design.\n\nContinue?""",'Are you sure?')
        if sanity.result == 1:
            filenamepath = os.path.join(os.path.dirname(__file__),"metadata.txt" )
            iniText = QSettings(filenamepath , QSettings.IniFormat)
            verno = str(iniText.value('version')) 
            from create_db import newdb
            newdbinstance = newdb(verno)
            if not newdbinstance.dbpath=='':
                db = newdbinstance.dbpath
                self.settingsdict['database'] = db
                self.saveSettings()

    def PlotTS(self):
        if self.settingsareloaded == False:    # If the first thing the user does is to plot time series, then load settings from project file    
            #utils.pop_up_info("reading from .qgs file")    #debugging
            self.loadSettings()    
        if not (self.settingsdict['database'] == '' or self.settingsdict['tstable'] =='' or self.settingsdict['tscolumn'] == ''):
            layer = qgis.utils.iface.activeLayer()
            if layer:
                if utils.selection_check(layer) == 'ok':
                    dlg = TimeSeriesPlot(self.iface, layer, self.settingsdict)
            else:
                utils.pop_up_info("You have to select a layer first!")
        else:
            utils.pop_up_info("Check Midvatten settings! \nSelect database, table and column for time series plot!")
            
    def PlotStratigraphy(self):            
        if self.settingsareloaded == False:    # If the first thing the user does is to plot stratigraphy, then load settings from project file
            self.loadSettings()    
        if not (self.settingsdict['database'] == '') and not (self.settingsdict['stratigraphytable']==''):
            layer = qgis.utils.iface.activeLayer()
            if layer:
                if utils.selection_check(layer) == 'ok' and utils.strat_selection_check(layer) == 'ok':
                        dlg = Stratigraphy(self.iface, layer, self.settingsdict)
                        dlg.showSurvey()
                        self.dlg = dlg        # only to prevent the Qdialog from closing.
            else:
                utils.pop_up_info("You have to select a layer first!")
        else: 
            utils.pop_up_info("Check Midvatten settings! \nYou have to select database and stratigraphy table first!")

    def PlotXY(self):            
        if self.settingsareloaded == False:    # If the first thing the user does is to plot xy data, then load settings from project file
            self.loadSettings()    
        if not (self.settingsdict['database'] == '' or self.settingsdict['xytable'] =='' or self.settingsdict['xy_xcolumn'] == '' or (self.settingsdict['xy_y1column'] == '' and self.settingsdict['xy_y2column'] == '' and self.settingsdict['xy_y3column'] == '')):
            layer = qgis.utils.iface.activeLayer()
            if layer:
                if utils.selection_check(layer) == 'ok':
                    dlg = XYPlot(self.iface, layer, self.settingsdict)
            else:
                utils.pop_up_info("You have to select a layer first!")
        else:
            utils.pop_up_info("Check Midvatten settings! \nSelect database, table and columns for x and y data!")

    def resetSettings(self):    
        self.settingsdict = self.createsettingsdict()    # calling for the method that defines an empty dictionary of settings
        self.saveSettings()        # the empty settings dictionary is stored

    def saveSettings(self):# settingsdict is a dictionary belonging to instance midvatten. Must be stored and loaded here.
        if not self.readingSettings:
            for (key, value) in self.settingsdict.items():        # For storing in project file, as Time Manager plugin
                try: # write plugin settings to QgsProject # For storing in project file, as Time Manager plugin
                    QgsProject.instance().writeEntry("Midvatten",key, value ) # For storing in project file, as Time Manager plugin
                except TypeError: # For storing in project file, as Time Manager plugin
                    utils.pop_up_info("Wrong type for "+key+"!\nType: "+str(type(value))) #For storing in project file, as Time Manager plugin
        
    def setup(self):
        """Choose spatialite database and relevant table"""
        if self.settingsareloaded == False:    # If the first thing the user does is to check settings, then load settings from project file
            self.loadSettings()    
        dlg = midvsettings(self.iface.mainWindow(), self.settingsdict)  # dlg is an instance of midvsettings
        if dlg.exec_() == QDialog.Accepted:      # When the settins dialog is closed, all settings are stored in the dictionary
            self.settingsdict['database'] = dlg.txtpath.text()    
            self.settingsdict['tstable'] = dlg.ListOfTables.currentText()
            self.settingsdict['tscolumn'] = dlg.ListOfColumns.currentText()
            self.settingsdict['tsdotmarkers'] = dlg.checkBoxDataPoints.checkState()
            self.settingsdict['tsstepplot'] = dlg.checkBoxStepPlot.checkState()
            self.settingsdict['xytable']  = dlg.ListOfTables_2.currentText()
            self.settingsdict['xy_xcolumn'] = dlg.ListOfColumns_2.currentText()
            self.settingsdict['xy_y1column'] = dlg.ListOfColumns_3.currentText()
            self.settingsdict['xy_y2column'] = dlg.ListOfColumns_4.currentText()
            self.settingsdict['xy_y3column'] = dlg.ListOfColumns_5.currentText()
            self.settingsdict['xydotmarkers'] =  dlg.checkBoxDataPoints_2.checkState()
            self.settingsdict['wqualtable']  = dlg.ListOfTables_WQUAL.currentText()
            self.settingsdict['wqual_paramcolumn'] = dlg.ListOfColumns_WQUALPARAM.currentText()
            self.settingsdict['wqual_valuecolumn'] = dlg.ListOfColumns_WQUALVALUE.currentText()
            self.settingsdict['wqual_unitcolumn'] = dlg.ListOfColumns_WQUALUNIT.currentText()
            self.settingsdict['wqual_sortingcolumn'] = dlg.ListOfColumns_WQUALSORTING.currentText()
            self.settingsdict['stratigraphytable'] = dlg.ListOfTables_3.currentText()
            self.settingsdict['tabwidget'] = dlg.tabWidget.currentIndex()
            self.saveSettings()            # Since the SelectTSDialog has saved all settings they should be reached by loading them here...

    def updatecoord(self):
        if self.settingsareloaded == False:    # If the first thing the user does is to update coordinates, then load settings from project file    
            self.loadSettings()    
        layer = self.iface.activeLayer()
        if not layer:           #check there is actually a layer selected
            utils.pop_up_info("You have to select/activate obs_points layer!")
        elif layer.isEditable():
            utils.pop_up_info("The selected layer is currently in editing mode.\nPlease exit this mode before updating coordinates.", "Warning")
        else:
            if not (self.settingsdict['database'] == ''):
                layer = qgis.utils.iface.activeLayer()
                if layer.name()==u'obs_points':     #IF LAYER obs_points IS SELECTED
                    sanity = utils.askuser("AllSelected","""Do you want to update coordinates\nfor All or Selected objects?""")
                    if sanity.result == 0:      #IF USER WANT ALL OBJECTS TO BE UPDATED
                        sanity = utils.askuser("YesNo","""Sanity check! This will alter the database.\nCoordinates will be written in fields east and north\nfor ALL objects in the obs_points table.\nProceed?""")
                        if sanity.result==1:
                            ALL_OBS = utils.sql_load_fr_db("select distinct obsid from obs_points")#a list of unicode strings is returned
                            observations = [None]*len(ALL_OBS)
                            i = 0
                            for obs in ALL_OBS:
                                observations[i] = obs[0]
                                i+=1
                            from coords_and_position import updatecoordinates
                            updatecoordinates(observations)
                    elif sanity.result == 1:    #IF USER WANT ONLY SELECTED OBJECTS TO BE UPDATED
                        sanity = utils.askuser("YesNo","""Sanity check! This will alter the database.\nCoordinates will be written in fields east and north\nfor SELECTED objects in the obs_points table.\nProceed?""")
                        if sanity.result==1:
                            if utils.selection_check(layer) == 'ok':    #Checks that there are some objects selected at all!
                                observations = utils.getselectedobjectnames()#a list of unicode strings is returned
                                from coords_and_position import updatecoordinates
                                updatecoordinates(observations)                        
                else:
                    utils.pop_up_info("You have to select/activate obs_points layer!")
            else:
                utils.pop_up_info("Check settings! \nSelect database first!")        

    def updateposition(self):
        if self.settingsareloaded == False:    # If the first thing the user does is to update coordinates, then load settings from project file    
            self.loadSettings()    
        layer = self.iface.activeLayer()
        if not layer:           #check there is actually a layer selected
            utils.pop_up_info("You have to select/activate obs_points layer!")
        elif layer.isEditable():
            utils.pop_up_info("The selected layer is currently in editing mode.\nPlease exit this mode before updating position.", "Warning")
        else:
            if not (self.settingsdict['database'] == ''):
                layer = qgis.utils.iface.activeLayer()
                if layer.name()==u'obs_points':     #IF LAYER obs_points IS SELECTED
                    sanity = utils.askuser("AllSelected","""Do you want to update position\nfor All or Selected objects?""")
                    if sanity.result == 0:      #IF USER WANT ALL OBJECTS TO BE UPDATED
                        sanity = utils.askuser("YesNo","""Sanity check! This will alter the database.\nALL objects in obs_points will be moved to positions\ngiven by their coordinates in fields east and north.\nProceed?""")
                        if sanity.result==1:
                            ALL_OBS = utils.sql_load_fr_db("select distinct obsid from obs_points")
                            observations = [None]*len(ALL_OBS)
                            i = 0
                            for obs in ALL_OBS:
                                observations[i] = obs[0]
                                i+=1
                            from coords_and_position import updateposition
                            updateposition(observations)
                            layer.updateExtents()
                    elif sanity.result == 1:    #IF USER WANT ONLY SELECTED OBJECTS TO BE UPDATED
                        sanity = utils.askuser("YesNo","""Sanity check! This will alter the database.\nSELECTED objects in obs_points will be moved to positions\ngiven by their coordinates in fields east and north.\nProceed?""")
                        if sanity.result==1:
                            if utils.selection_check(layer) == 'ok':    #Checks that there are some objects selected at all!
                                observations = utils.getselectedobjectnames()
                                from coords_and_position import updateposition
                                updateposition(observations)
                                layer.updateExtents()
                else:
                    utils.pop_up_info("You have to select/activate obs_points layer!")
            else:
                utils.pop_up_info("Check settings! \nSelect database first!")        
            
    def waterqualityreport(self):
        if self.settingsareloaded == False:    # If the first thing the user does is to plot time series, then load settings from project file
            self.loadSettings()    
        if not (self.settingsdict['database'] == '') and not (self.settingsdict['wqualtable']=='') and not (self.settingsdict['wqual_paramcolumn']=='')  and not (self.settingsdict['wqual_valuecolumn']==''):
            if qgis.utils.iface.activeLayer():
                if utils.selection_check(qgis.utils.iface.activeLayer()) == 'ok':#there is a field obsid and at least one object is selected
                    fail = 0
                    for k in utils.getselectedobjectnames():#all selected objects
                        if not utils.sql_load_fr_db("select obsid from %s where obsid = '%s'"%(self.settingsdict['wqualtable'],str(k))):#if there is a selected object withou water quality data
                            self.iface.messageBar().pushMessage("Error","No water quality data for %s"%str(k), 2)
                            fail = 1
                    if not fail == 1:#only if all objects has data
                        wqualreport(qgis.utils.iface.activeLayer(),self.settingsdict)            #TEMPORARY FOR GVAB
            else:
                utils.pop_up_info("You have to select a layer and the object with water quality first!")
        else: 
            utils.pop_up_info("Check Midvatten settings! \nSomething is wrong in the 'W quality report' tab!")

    def wlvlcalculate(self):             
        errorsignal = 0
        if self.settingsareloaded == False:    # If this is the first does - then load settings from project file
            self.loadSettings()    
            
        allcritical_layers = ('obs_points', 'w_levels')     #Check that none of these layers are in editing mode
        for layername in allcritical_layers:
            layerexists = utils.find_layer(str(layername))
            if layerexists:
                if layerexists.isEditable():
                    utils.pop_up_info("Layer " + str(layerexists.name()) + " is currently in editing mode.\nPlease exit this mode before calculating water level.", "Warning")
                    errorsignal = 1

        if self.settingsdict['database'] == '': #Check that database is selected
            utils.pop_up_info("Check settings! \nSelect database first!")        
            errorsignal = 1

        layer = qgis.utils.iface.activeLayer()
        if layer:
            if utils.selection_check(layer) == 'ok':
                pass
            else:
                errorsignal = 1
        else:
            utils.pop_up_info("You have to select a relevant layer!")
            errorsignal = 1

        if not(errorsignal == 1):     
            from wlevels_calc_calibr import calclvl
            dlg = calclvl(self.iface.mainWindow())  # dock is an instance of calibrlogger
            dlg.exec_()

    def wlvlloggcalibrate(self):             
        errorsignal = 0
        if self.settingsareloaded == False:    # If this is the first does - then load settings from project file
            self.loadSettings()    

        allcritical_layers = ('w_levels_logger', 'w_levels')     #Check that none of these layers are in editing mode
        for layername in allcritical_layers:
            layerexists = utils.find_layer(str(layername))
            if layerexists:
                if layerexists.isEditable():
                    utils.pop_up_info("Layer " + str(layerexists.name()) + " is currently in editing mode.\nPlease exit this mode before calibrating logger data.", "Warning")
                    errorsignal = 1

        layer = qgis.utils.iface.activeLayer()
        if layer:
            if utils.selection_check(layer) == 'ok':
                pass
            else:
                errorsignal = 1
        else:
            utils.pop_up_info("You have to select a relevant layer!")
            errorsignal = 1
            
        if errorsignal == 0:
            if not (self.settingsdict['database'] == ''):
                if qgis.utils.iface.activeLayer():
                    if utils.selection_check(qgis.utils.iface.activeLayer(),1) == 'ok':
                        obsid = utils.getselectedobjectnames()
                        sanity1sql = """select count(obsid) from w_levels_logger where obsid = '""" +  obsid[0] + """'"""
                        sanity2sql = """select count(obsid) from w_levels_logger where head_cm not null and head_cm !='' and obsid = '""" +  obsid[0] + """'"""
                        if utils.sql_load_fr_db(sanity1sql) == utils.sql_load_fr_db(sanity2sql): # This must only be done if head_cm exists for all data
                            from wlevels_calc_calibr import calibrlogger
                            dlg = calibrlogger(self.iface.mainWindow(),obsid)  # dock is an instance of calibrlogger
                            dlg.exec_()
                        else:
                            utils.pop_up_info("""There must not be empty cells or null values in the 'head_cm' column!\nFix head_cm data problem and try again.""", "Error") 
                else:
                    utils.pop_up_info("You have to select the obs_points layer and the object (just one!) for which logger data is to be imported!")
            else: 
                utils.pop_up_info("Check settings! \nYou have to select database first!")
