from setuptools import setup, find_packages

VERSION = '1.0.1' 
DESCRIPTION = 'Animal tracking data source & formatter'
LONG_DESCRIPTION = 'Python package that sources animal tracking data from the Movebank and Anitra platforms'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="animaltrackingdata", 
        version=VERSION,
        author="Karel Douda",
        author_email="karel.douda@anitra.cz",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["requests", "XlsxWriter"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        keywords=['anitra', 'movebank', "animal tracking", "animal data"],
        classifiers= [
            "Development Status :: 3 - Alpha"
        ]
)