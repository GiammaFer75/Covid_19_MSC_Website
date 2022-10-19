# For running Flask on the ACER ---> https://stackoverflow.com/questions/51119495/how-to-setup-environment-variables-for-flask-run-on-windows
#
# set FLASK_ENV=development        -------> suddenly it needs also this
# set FLASK_APP=Cov19_msc_V1.py
# $env:FLASK_APP = "Cov19_msc_V1.py"
# set FLASK_DEBUG=1
# $env:FLASK_DEBUG = 1
#
# run flask

# TO FIX THE ISSUES WITH ANACONDA IDE
# https://www.linkedin.com/pulse/building-data-science-website-flask-venvanaconda-part1-sushant-rao/
# 
# Open a TERMINL in Jupiter Lab
# Launch python <yourapp>.py
# 
# Remember that (debug=True, host="0.0.0.0", port=5000) must be specified into the .py file and not set in the environment as in 
# the previous method.

from flask import Flask, render_template, url_for
import os, sqlalchemy

IMAGE_FOLDER = os.path.join('../static', 'Images')

Cov19_msc = Flask(__name__)
Cov19_msc.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

@Cov19_msc.route("/")
@Cov19_msc.route("/Home")
def home_page():
	logo_filename = os.path.join(Cov19_msc.config['UPLOAD_FOLDER'], 'cropped-Covid19-MSC.png')
	return render_template("Home.html", logo_image = logo_filename)

@Cov19_msc.route("/page1")
def page1():
    return render_template("page1.html")

if __name__ == "__main__":
    Cov19_msc.run(debug=True, host="0.0.0.0", port=5050)