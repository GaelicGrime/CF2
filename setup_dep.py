

#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of CSCF.setup.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


from setuptools import find_packages
from setuptools import setup


setup(
  author="GaelicGrime",
  author_email="will.angus.blaylock@gmail.com",
  license="GPLv3",
  name="CSCF",
  provides="CSCF",
  url="https://github.com/ComfortableSoftware/commonFunctions_py",
  version="0.2.3",
  package_dir={"CSCF": "CSCF"},
  package_data={
      "CSCF": [
          "../doc/*",
          "CLASSES_D/*",
          "CONST_D/*",
          "SUBM_D/*",
      ]
  },
  packages=find_packages(),
  install_requires=[
  ],
  extras_require={
      "hashing": ["hashlib"],
      "pickling": ["pickle"],
      "databases": ["mysql"],
      "time-date-stuff": [
          "datedelta",
          "datetime",
          "dateutil",
          "time",
      ],
      "debugging": [
          "inspect",
      ],
  }
)
