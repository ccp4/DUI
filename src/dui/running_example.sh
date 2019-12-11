################################### dials 1.xxx
#
# dials.import /scratch/dui_test/only_9_img/X4_wide_M1S4_2_*.cbf output.datablock=1_datablock.json output.log=1_import.log output.debug_log=1_import.debug.log
# dials.find_spots spotfinder.mp.nproc=8 input.datablock=1_datablock.json output.datablock=2_datablock.json output.reflections=2_reflections.pickle output.log=2_find_spots.log output.debug_log=2_find_spots.debug.log
# dials.index input.datablock=2_datablock.json input.reflections=2_reflections.pickle output.experiments=3_experiments.json output.reflections=3_reflections.pickle output.log=3_index.log output.debug_log=3_index.debug.log
# dials.refine_bravais_settings input.experiments=3_experiments.json input.reflections=3_reflections.pickle output.prefix=lin_4_ output.log=4_refine_bravais_settings.log output.debug_log=4_refine_bravais_settings.debug.log
# dials.reindex input.reflections=3_reflections.pickle change_of_basis_op=b,c,a output.reflections=5_reflections.pickle
# dials.refine input.experiments=lin_4_bravais_setting_9.json input.reflections=5_reflections.pickle output.experiments=6_experiments.json output.reflections=6_reflections.pickle output.log=6_refine.log output.debug_log=6_refine.debug.log
# dials.integrate integration.mp.nproc=8 input.experiments=6_experiments.json input.reflections=6_reflections.pickle output.experiments=7_experiments.json output.reflections=7_reflections.pickle output.phil=7_integrate.phil output.log=7_integrate.log output.debug_log=7_integrate.debug.log
#
#################################### dials 2.0

dials.import /scratch/dui_test/only_9_img/X4_wide_M1S4_2_*.cbf output.experiments=1_experiment.expt output.log=1_import.log
dials.find_spots spotfinder.mp.nproc=8 input.experiments=1_experiment.expt output.experiments=2_experiment.expt output.reflections=2_reflections.refl output.log=2_find_spots.log
dials.index input.experiments=2_experiment.expt input.reflections=2_reflections.refl output.experiments=3_experiments.expt output.reflections=3_reflections.refl output.log=3_index.log
dials.refine_bravais_settings input.experiments=3_experiments.expt input.reflections=3_reflections.refl output.prefix=lin_4_ output.log=4_refine_bravais_settings.log
dials.reindex input.reflections=3_reflections.refl change_of_basis_op=b,c,a output.reflections=5_reflections.refl
dials.refine input.experiments=lin_4_bravais_setting_9.expt input.reflections=5_reflections.refl output.experiments=6_experiments.expt output.reflections=6_reflections.refl output.log=6_refine.log
dials.integrate integration.mp.nproc=8 input.experiments=6_experiments.expt input.reflections=6_reflections.refl output.experiments=7_experiments.expt output.reflections=7_reflections.refl output.phil=7_integrate.phil output.log=7_integrate.log

