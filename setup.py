from setuptools import setup

setup(name ="Smart Trash Can",
      version ="Alpha 1.0",
      description ="Packages to be installed: Distance sensor, OLED etc",
      author ="Fahim Ahmed", "Amolak Plaha",
      packages = luma.core(), pathlib(), PIL(), 
      py_modules=["ds"],["text_display"],
     )
