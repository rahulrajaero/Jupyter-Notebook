# Install a Package Globally
# Once a package is created, it can be installed for system wide use by running the setup script. 
# The script calls setup() function from setuptools module.

from setuptools import setup

setup(name = "mypackage", 
        version = '0.1',
        description = 'Testing installlation of package',
        url = '#',
        author = 'rahul',
        author_email = 'rahulraj.jr7@gmail.com',
        license = 'MIT',
        packages = ['mypackage'],
        zip_safe = False)

# Now execute the following command to install mypack using the pip utility. 
# Ensure that the command prompt is in the parent folder, in this case D:\MyApp.

# -------------- RUN THIS ----------------------------------------
#--------------- D:\MyApp>pip install .  ------------------------