# As initialisation file, it is in charge to import the modules needed in order to run the others scripts.
from flask import Flask, render_template, url_for 
import os

Cov19_msc = Flask(__name__)


# Set the directory for the images
IMAGE_FOLDER = os.path.join('../static', 'Images')
Cov19_msc.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

# In 'routes' there are all the instances for the webpages
from WebsitePackage import routes