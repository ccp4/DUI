"""
low level handling info for outputs in DUI

Author: Luis Fuentes-Montero (Luiso)
With strong help from DIALS and CCP4 teams

copyright (c) CCP4 - DLS
"""

import json
import logging
import pickle
import sys

from dials.array_family import flex
#from dxtbx.datablock import DataBlockFactory
from dxtbx.model import Experiment, ExperimentList
from dxtbx.model.experiment_list import (
    ExperimentListFactory,
    InvalidExperimentListError,
)

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


logger = logging.getLogger(__name__)


class InfoData:
    def __init__(self):

        self.a = None
        self.b = None
        self.c = None
        self.alpha = None
        self.beta = None
        self.gamma = None
        self.spg_group = None

        self.r1 = None
        self.r2 = None
        self.r3 = None

        self.xb = None
        self.yb = None
        self.dd = None
        self.n_pan_xb_yb = None

        self.w_lambda = None

        self.img_ran1 = None
        self.img_ran2 = None
        self.oscil1 = None
        self.oscil2 = None
        self.e_time = None

        self.n_pans = None
        self.x_px_size = None
        self.y_px_size = None
        self.gain = None
        self.max_res = None

        self.n_strng = None
        self.n_index = None
        self.n_refnd = None
        self.n_integ_sum = None
        self.n_integ_prf = None

        self.tmpl_str = None
        self.ref2exp = None

        self.np_mask = None
        self.mask_flex = None


def update_all_data(reflections_path=None, experiments_path=None):
    dat = InfoData()
    dat.ref2exp = None

    if reflections_path is not None:

        try:
            refl_tabl = flex.reflection_table.from_file(reflections_path)
            dat.n_strng = refl_tabl.get_flags(refl_tabl.flags.strong).count(True)
            dat.n_index = refl_tabl.get_flags(refl_tabl.flags.indexed).count(True)
            dat.n_refnd = refl_tabl.get_flags(refl_tabl.flags.used_in_refinement).count(
                True
            )
            dat.n_integ_sum = refl_tabl.get_flags(refl_tabl.flags.integrated_sum).count(
                True
            )
            dat.n_integ_prf = refl_tabl.get_flags(refl_tabl.flags.integrated_prf).count(
                True
            )

        except BaseException as e:
            # We don't want to catch bare exceptions but don't know
            # what this was supposed to catch. Log it.
            logger.info(
                " >> Caught unknown exception type: %s, %s", type(e).__name__, e
            )

            logger.info("failed to find reflections")
            logger.info("reflections_path = %s", reflections_path)

    if experiments_path is not None:
        try:
            experiments = ExperimentListFactory.from_json_file(
                experiments_path, check_format=False
            )
        except InvalidExperimentListError as e:
            # Commonly this happens when given a refine_bravais_settings summary file
            if not experiments_path.endswith("_bravais_summary.json"):
                logger.info("Got invalid experiment list %s: %s", experiments_path, e)

        except BaseException as e:
            # We don't want to catch bare exceptions but don't know
            # what this was supposed to catch. Log it.
            logger.info("exception #1 %s: %s", type(e).__name__, e)

            # TODO Maybe the next try block is not needed, consider removing all

            try:
                # FIXME here only take the first datablock. What if there are more?
                Deprecated_code = '''
                datablock = DataBlockFactory.from_serialized_format(
                    experiments_path, check_format=False
                )[0]

                # FIXME here only take the first model from each
                beam = datablock.unique_beams()[0]
                detector = datablock.unique_detectors()[0]
                scan = datablock.unique_scans()[0]

                # build a pseudo ExperimentList (with empty crystals)
                experiments = ExperimentList()
                experiments.append(Experiment(beam=beam, detector=detector, scan=scan))
                '''
                experiments = ExperimentList.from_file(
                    experiments_path
                )

            except ValueError:
                logger.info("failed to read json file")
                logger.info("experiments_path = %s", experiments_path)
                return dat

        try:
            imageset_tmp = experiments.imagesets()[0]
            mask_file = imageset_tmp.external_lookup.mask.filename

            pick_file = open(mask_file, "rb")
            mask_tup_obj = pickle.load(pick_file)
            pick_file.close()

            dat.mask_flex = mask_tup_obj[0]
            mask_np_arr = dat.mask_flex.as_numpy_array()
            dat.np_mask = mask_np_arr

        except OSError:
            logger.info("No mask in this node")
            dat.np_mask = None
            dat.mask_flex = None

        # FIXME it takes just the first experiment. What if there are more?
        exp = experiments[0]

        # Get crystal data
        if exp.crystal is not None:
            unit_cell = exp.crystal.get_unit_cell()
            dat.a, dat.b, dat.c, dat.alpha, dat.beta, dat.gamma = unit_cell.parameters()

            exp_crystal = exp.crystal
            logger.info("exp_crystal =  %s", exp_crystal)
            b_mat = exp.crystal.get_B()
            dat.b11 = b_mat[0]
            dat.b12 = b_mat[1]
            dat.b13 = b_mat[2]
            dat.b21 = b_mat[3]
            dat.b22 = b_mat[4]
            dat.b23 = b_mat[5]
            dat.b31 = b_mat[6]
            dat.b32 = b_mat[7]
            dat.b33 = b_mat[8]

            sg = str(exp.crystal.get_space_group().info())
            logger.info("spgr =  %s", sg)
            dat.spg_group = sg

            from scitbx import matrix

            u_mat = matrix.sqr(exp.crystal.get_U())

            dat.u11 = b_mat[0]
            dat.u12 = b_mat[1]
            dat.u13 = b_mat[2]
            dat.u21 = b_mat[3]
            dat.u22 = b_mat[4]
            dat.u23 = b_mat[5]
            dat.u31 = b_mat[6]
            dat.u32 = b_mat[7]
            dat.u33 = b_mat[8]

            rot_angs = u_mat.r3_rotation_matrix_as_x_y_z_angles(deg=True)
            logger.info("u_mat = %s", u_mat)

            logger.info("rot_angs = %s", rot_angs)
            dat.r1, dat.r2, dat.r3 = rot_angs

        # Get beam data
        dat.w_lambda = exp.beam.get_wavelength()

        # Get detector data
        # assume details for the panel the beam intersects are the same
        # for the whole detector
        # TODO fix it for I23

        pnl_beam_intersects, (beam_x, beam_y) = exp.detector.get_ray_intersection(
            exp.beam.get_s0()
        )
        pnl = exp.detector[pnl_beam_intersects]
        logger.info("beam_x, beam_y = %s %s", beam_x, beam_y)

        dat.n_pan_xb_yb = pnl_beam_intersects
        dat.xb = beam_x
        dat.yb = beam_y

        dist = pnl.get_distance()

        logger.info("pnl_beam_intersects              %s", pnl_beam_intersects)
        logger.info("dist                             %s", dist)

        dat.dd = dist

        dat.img_ran1, dat.img_ran2 = exp.scan.get_image_range()
        dat.oscil1, dat.oscil2 = exp.scan.get_oscillation()

        # is the next line right? check what dials.show does
        dat.e_time = max(exp.scan.get_exposure_times())

        dat.n_pans = len(exp.detector)
        dat.x_px_size, dat.y_px_size = pnl.get_pixel_size()
        dat.gain = pnl.get_gain()
        dat.max_res = exp.detector.get_max_resolution(exp.beam.get_s0())

        # manually finding template from experiments_path

        try:
            with open(experiments_path) as infile:
                json_info = json.load(infile)

            if type(json_info) is dict:
                imageset = json_info["imageset"]

            elif type(json_info) is list:
                imageset = json_info[0]["imageset"]

            dat.tmpl_str = imageset[0]["template"]

            logger.info("dat.tmpl_str = %s", dat.tmpl_str)

        except (KeyError, IndexError):
            logger.info("failed to find template in JSON file")

        dat.ref2exp = exp

    return dat


if __name__ == "__main__":
    # This should be called with two paths adden in console
    update_all_data(reflections_path=sys.argv[1], experiments_path=sys.argv[2])
