from setuptools import setup
import os

# Read the DUI version out of a version file in the package
_ver_file = os.path.join(os.path.dirname(__file__), "src", "dui", "_version.py")
_ver_locals = {}
exec(open(_ver_file).read(), _ver_locals)
DUI_VERSION = _ver_locals["__version__"]

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
)

# TODO(nick): Work out how to get requirements working, including non-pip like PyQT
# install_requires=['PyQt4','psutil', 'numpy'],
