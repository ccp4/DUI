import os
import subprocess
from glob import glob

from setuptools import Command, setup

# Read the DUI version out of a version file in the package
_ver_file = os.path.join(os.path.dirname(__file__), "src", "dui", "_version.py")
_ver_locals = {}
exec(open(_ver_file).read(), _ver_locals)
DUI_VERSION = _ver_locals["__version__"]

# Borrowed from: https://github.com/glue-viz/glue/blob/master/setup.py
# Copyright (c) 2013, Glue developers


# Based off https://gist.github.com/ivanalejandro0/6758741
class BuildQt(Command):
    """
    Defines a command for setup.py that compiles the *.ui and *.qrc files
    into python files.
    It looks for *.ui files in _UI_PATH subfolder.
    """

    _UI_PATH = os.path.join("src", "dui", "resources")

    user_options = [("uic=", "u", "Custom uic command (usually pyside-uic or pyuic4)")]

    def initialize_options(self):
        """
        Sets the proper command names for the compiling tools.
        """
        self.pyuic = "pyside2-uic"

    def finalize_options(self):
        pass

    def _compile_ui(self, infile, outfile):
        try:
            subprocess.call([self.pyuic, infile, "-o", outfile])
        except OSError:
            print("uic command failed - make sure that pyside-uic " "is in your $PATH")

    def run(self):
        # compile ui files
        for infile in glob(os.path.join(self._UI_PATH, "*.ui")):
            directory, ui_filename = os.path.split(infile)
            py_filename = ui_filename.replace(".ui", ".py")
            outfile = os.path.join(directory, "ui_" + py_filename)
            print("Compiling: {0} -> {1}".format(infile, outfile))
            self._compile_ui(infile, outfile)


setup(
    name="dui",
    version=DUI_VERSION,
    license="GPL 2.0",
    description="Dials User Interface",
    author="Luis Fuentes-Montero (Luiso)",
    author_email="luis.fuentes-montero@diamond.ac.uk",
    url="https://github.com/ccp4/DUI",
    platforms="GNU/Linux & Mac OS",
    packages=["dui", "dui.outputs_n_viewers"],
    package_dir={"": "src"},
    data_files=[
        (
            "dui/resources",
            [
                "src/dui/resources/DIALS_Logo_smaller_centred_grayed.png",
                "src/dui/resources/DIALS_Logo_smaller_centred.png",
                "src/dui/resources/find_spots_grayed.png",
                "src/dui/resources/find_spots.png",
                "src/dui/resources/import_grayed.png",
                "src/dui/resources/import.png",
                "src/dui/resources/index_grayed.png",
                "src/dui/resources/index.png",
                "src/dui/resources/integrate_grayed.png",
                "src/dui/resources/integrate.png",
                "src/dui/resources/refine_grayed.png",
                "src/dui/resources/refine.png",
                "src/dui/resources/reindex_grayed.png",
                "src/dui/resources/reindex.png",
                "src/dui/resources/re_try_grayed.png",
                "src/dui/resources/re_try.png",
                "src/dui/resources/stop_grayed.png",
                "src/dui/resources/stop.png",
                "src/dui/resources/scale.png",
                "src/dui/resources/scale_grayed.png",
                "src/dui/resources/symmetry.png",
                "src/dui/resources/symmetry_grayed.png",
                "src/dui/resources/zoom_plus_ico.png",
                "src/dui/resources/zoom_ono_one_ico.png",
                "src/dui/resources/zoom_border.png",
                "src/dui/resources/zoom_minus_ico.png",
                "src/dui/resources/error_loading_dialog.ui",
                "src/dui/resources/export.png",
                "src/dui/resources/export_grayed.png",
                "src/dui/resources/first_img.png",
                "src/dui/resources/rew_img.png",
                "src/dui/resources/prev_img.png",
                "src/dui/resources/next_img.png",
                "src/dui/resources/ffw_img.png",
                "src/dui/resources/last_img.png",
            ],
        )
    ],
    include_package_data=True,
    entry_points={"console_scripts": ["dui=dui.main_dui:main"]},
    cmdclass={"build_qt": BuildQt},
)

# TODO(nick): Work out how to get requirements working, including non-pip like PyQT
# install_requires=['PyQt4','psutil', 'numpy'],
