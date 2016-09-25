# -*- coding: utf-8 -*-

"""
Last updated on 15/12/2014

@author: Cheng WANG
"""

import sys
import os
import time
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from medapIHM.medapMainWindow import MedapMainWindow
#from AnemoClinoIHM.AnalyserUsefulClasses.StartWindow import StartWindow
#from AnemoClinoContext.GlobalContext import *
#from AnemoClinoMediator.AnalyserMediator import *
from Image.qrc_resources import *
# cmd for convert png files to resource code: pyrcc4.exe -o qrc_resources.py resource.qrc


def main():
    """
        -- the main procedure to generate the graphical tool
    """

    # the graphical tool
    app = QApplication(sys.argv)

    logo = QPixmap(":logo2016.png")
    splash = QSplashScreen(logo)
    splash.show()

    time.sleep(2)

    app.setOrganizationName("Shenzhen institute of advanced technology")
    app.setApplicationName("Medical Data Processing Factory")
    app.setWindowIcon(QIcon(":/icon.png"))
    app.setStyle("cleanlooks")  # important, if not, icon can't adapt the size of button

    username = os.environ['USERNAME']
    workspace_path = 'C:\Users\\' + username + '\Documents\mdp\\'
    calibrated_files_path = workspace_path + 'calibrated_files\\'
    global_context_path = workspace_path + 'global_context\\'

    if not os.path.exists(workspace_path):
        os.mkdir(workspace_path)
        os.mkdir(calibrated_files_path)
        os.mkdir(global_context_path)
        '''
        w = StartWindow()
        while not w.get_configuration_state():
            w.exec_()
        '''
    '''
    # Model
    global_context = GlobalContext()
    global_context.set_workspace_path(workspace_path)
    global_context.set_calibrated_files_path(calibrated_files_path)
    global_context.set_global_context_path(global_context_path)
    global_context.set_user_name(username)

    # Controller
    analyseur_mediator = AnalyserMediator()
    analyseur_mediator.set_global_context(global_context)
    '''
    # View
    medapMainWindow = MedapMainWindow()
    #anemo_clino_analyseur.set_analyseur_mediator(analyseur_mediator)

    # execute the application
    medapMainWindow.show()

    splash.finish(medapMainWindow)

    app.exec_()


if __name__ == '__main__':
    main()
