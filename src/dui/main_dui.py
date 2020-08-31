"""
DUI's main Widget launcher

Author: Luis Fuentes-Montero (Luiso)
With strong help from DIALS and CCP4 teams

copyright (c) CCP4 - DLS
"""

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from __future__ import absolute_import, division, print_function

import argparse
import logging
import os
import sys
import signal

from dui.cli_utils import sys_arg

logger = logging.getLogger(__name__)


def main():
    # Process any command arguments
    parser = argparse.ArgumentParser(
        description="DUI, the dials GUI",
        usage="dui [-h|--help] [-v[v]][template=TEMPLATE] [directory=DIRECTORY]",
    )
    parser.add_argument("positionals", type=str, nargs="*", help=argparse.SUPPRESS)
    parser.add_argument("--verbose", "-v", action="count", default=0)
    args = parser.parse_args()

    # Set up the logger to only show warnings unless -v (info) or -vv (debug)
    assert args.verbose >= 0
    if args.verbose == 0:
        # By default, show INFO but without notation
        logging.basicConfig(level=logging.WARN, format="%(message)s")
    elif args.verbose == 1:
        # Verbose is same as default but has origin info
        logging.basicConfig(level=logging.INFO)
    elif args.verbose > 1:
        # More debug levels show everything
        logging.basicConfig(
            level=logging.DEBUG, format="%(levelname)s:%(name)s:%(lineno)s %(message)s"
        )

    # Turn things off unless at varying depths of verbosity
    if args.verbose <= 2:
        logging.getLogger("PyQt4.uic").setLevel(logging.WARNING)

    if args.verbose >= 2:
        logging.debug("Running debug out: ctrl-c will close application")
        signal.signal(signal.SIGINT, signal.SIG_DFL)

    # Process the phil-style parameters
    for arg in args.positionals[:]:
        if arg.startswith("template="):
            sys_arg.template = arg[len("template=") :]
            args.positionals.remove(arg)
        elif arg.startswith("directory="):
            sys_arg.directory = os.path.abspath(arg[len("directory=") :])
            args.positionals.remove(arg)

    # Warn if any remaining (unknown) parameters given
    if args.positionals:
        logger.warning(
            "Unknown parameter%s %s",
            "s" if len(args.positionals) > 1 else "",
            " ".join("'{}'".format(x) for x in args.positionals),
        )
        # Should we exit here? Maybe QT can handle it(???)

    logger.info("sys_arg.template =%s", sys_arg.template)
    logger.info("sys_arg.directory=%s", sys_arg.directory)

    # Inline import so that we can load this after logging setup

    from dui.gui_utils import loading_error_dialog
    from dui.m_idials_gui import DUIDataLoadingError, MainWidget
    from dui.qt import QApplication, QStyleFactory

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    logger.debug(
        "QT Style: %s [%s]", app.style().objectName(), ", ".join(QStyleFactory.keys())
    )

    try:
        ex = MainWidget()
    except DUIDataLoadingError as e:
        ex = loading_error_dialog(e.original_traceback)

    ex.show()

    # Needed for a QT4 bug(?) on mac - windows don't steal focus on open
    ex.activateWindow()
    ex.raise_()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
