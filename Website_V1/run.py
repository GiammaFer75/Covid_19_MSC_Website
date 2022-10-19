# From the package you have to import your Flask application
from WebsitePackage import Cov19_msc 

if __name__ == "__main__":
    Cov19_msc.run(debug=True, host="0.0.0.0", port=5050)