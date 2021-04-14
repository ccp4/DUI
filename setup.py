import pathlib
import subprocess
import sys

from setuptools import Command, setup


def _read_version() -> str:
    """Read the DUI version out of a version file in the package"""
    _ver_file = pathlib.Path(__file__).parent / "src" / "dui" / "_version.py"
    _ver_locals = {}
    exec(_ver_file.read_bytes(), _ver_locals)
    return _ver_locals["__version__"]


DUI_VERSION = _read_version()


# Based off https://gist.github.com/ivanalejandro0/6758741
class BuildQt(Command):
    """Command for setup.py to build QT ui and resource files"""

    # Source folders to search recursively
    _UI_PATH = pathlib.Path("src") / "dui" / "resources"
    _QRC_PATH = pathlib.Path("src") / "dui" / "resources"

    user_options = [
        ("pyrcc=", None, "pyrcc command executable"),
        ("pyuic=", None, "pyuic command executable"),
    ]

    def initialize_options(self):
        self.pyrcc = "pyside2-rcc"
        self.pyuic = "pyside2-uic"

    def finalize_options(self):
        pass

    def _compile_ui(self, infile: pathlib.Path, outfile: pathlib.Path):
        try:
            subprocess.call([self.pyuic, str(infile), "-x", "-o", str(outfile)])
        except OSError:
            sys.exit(
                f"uic command failed - make sure that {self.pyuic} is in your $PATH"
            )

    def _compile_rcc(self, infile: pathlib.Path, outfile: pathlib.Path):
        try:
            subprocess.call([self.pyrcc, str(infile), "-o", str(outfile)])
        except OSError:
            sys.exit(
                f"rcc command failed - make sure that {self.pyrcc} is in your $PATH"
            )

    def run(self):
        # Compile .ui files
        for infile in self._UI_PATH.glob("**/*.ui"):
            outfile = infile.parent / f"ui_{infile.stem}.py"
            print(f"Compiling: {infile} -> {outfile}")
            self._compile_ui(infile, outfile)
        # Compile .qrc files
        for infile in self._QRC_PATH.glob("**/*.qrc"):
            outfile = infile.parent / f"rc_{infile.stem}.py"
            print(f"Compiling: {infile} -> {outfile}")
            self._compile_rcc(infile, outfile)


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
