from main import *
import json
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import subprocess
#from shareplum import Site, Office365, folder
#from shareplum.site import Version

import json, os


class Exporter(MainWindow):
    
    def onInitUploadModule(self):
        Functions.read_uploadprefeneces(self)       
        self.ui.xmlFilePath.setText('{}'.format(config.EXPORTER_PREFERENCES["EXPORTER_PARAMETERS"]["XML_FILE_PATH"]))

    def open_file_dialog(self):        
        qfd = QFileDialog()
        path = ""
        filter = "xml(*.xml)"
        f = QFileDialog.getOpenFileName(qfd, "Select XML file to process", path, filter)
        self.ui.xmlFilePath.setText('{}'.format(f[0]))

    def excute_extracter(self):
        p = subprocess.run([config.EXPORTER_PREFERENCES["EXPORTER_PARAMETERS"]["BAT_FILE_PATH"], self.ui.xmlFilePath.toPlainText()], capture_output=True)
        logging.info("Output Message...")
        logging.info(print(p.stdout.decode()))
        logging.info("Error Message...")
        logging.info(print(p.stderr.decode()))

class Functions(MainWindow):
    def read_uploadprefeneces(self):
        try:
            # Opening JSON file
            logging.info("--Opening preference file--")             
            f = open('exporterpreference.json',) 
  
            # returns JSON object as  
            # a dictionary 
            config.EXPORTER_PREFERENCES = json.load(f)        
            
        except FileNotFoundError:
            logging.exception("exporter Preference file not found")            
        finally:
            f.close()

    

class SharePoint(MainWindow):

    def initShareData(self):
        #ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        #config_path = '\\'.join([ROOT_DIR, 'config.json'])
        logging.info("--Opening preference file--")             
        f = open('config.json',)
        configuration = json.load(f)
        configuration = configuration['share_point']
        # read config file
        #with open(config_path) as config_file:
            #configuration = json.load(f)
            #configuration = configuration['share_point']

        config.USERNAME = configuration['user']
        config.PASSWORD = configuration['password']
        config.SHAREPOINT_URL = configuration['url']
        config.SHAREPOINT_SITE = configuration['site']
        config.SHAREPOINT_DOC = configuration['doc_library']   

    def auth(self):
        self.timeout = None
        self.authcookie = Office365(config.SHAREPOINT_URL, username=config.USERNAME, password=config.PASSWORD).GetCookies()
        self.site = Site(config.SHAREPOINT_SITE, version=Version.v365, authcookie=self.authcookie)

        return self.site

    def connect_folder(self, folder_name):
        self.auth_site = SharePoint.auth(self)
        self.timeout = None        
        self.sharepoint_dir = '/'.join([config.SHAREPOINT_DOC, folder_name])
        self.sharepoint_dir = self.sharepoint_dir #+ "/" + "091121"
        self.folder = self.auth_site.Folder(self.sharepoint_dir)

        return self.folder

    def upload_folder(self, folder_name, dir_path):
        uploadFileNames = []
        lockfiles = []
        #Functions.initShareData(self)
        for root, dirs, files in os.walk(dir_path, topdown=False):
            for name in files:
                fname=os.path.join(root, name)
                if not name.endswith(".idlk"):
                    uploadFileNames.append(fname)
                else:
                    lockfiles.append(fname)

        for filename in uploadFileNames:
            filefoldername = filename.replace((dir_path+'\\'), '')
            indexofbackslash = filefoldername.rfind('\\')

            if indexofbackslash > 0:
                foldername = filefoldername[0:indexofbackslash]
                file_name = filefoldername[indexofbackslash+1:]
            else:
                file_name = filefoldername
                foldername = ""

            with open(filename, mode='rb') as file_obj:
                file_content = file_obj.read()

            if not foldername:
                foldername = folder_name
            else:
                foldername = folder_name+'/'+foldername
            self._folder = SharePoint.connect_folder(self,foldername)
            self._folder.upload_file(file_content, file_name)            
                    

    def upload_file(self, file, file_name, folder_name):
        self._folder = self.connect_folder(folder_name)

        with open(file, mode='rb') as file_obj:
            file_content = file_obj.read()

        self._folder.upload_file(file_content, file_name)
     

    def delete_file(self, file_name, folder_name):

        self._folder = self.connect_folder(folder_name)

        self._folder.delete_file(file_name)




         