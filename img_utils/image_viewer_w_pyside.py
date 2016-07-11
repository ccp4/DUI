#!/usr/bin/env python
#
# image_viewer.py
#
#  Copyright (C) 2013 Diamond Light Source
#
#  Exercise starting from Richard Gildea's image_viewer.py command line
#

from __future__ import division
from dials.array_family import flex # import dependency


if __name__ == '__main__':

    from dials.util.options import OptionParser
    from dials.util.options import flatten_datablocks
    import libtbx.load_env

    usage_message = """
     %s datablock.json [reflections.pickle]
     """ %libtbx.env.dispatcher_name
    parser = OptionParser(usage=usage_message,
                          read_datablocks=True,
                          read_datablocks_from_images=True)

    params, options = parser.parse_args(show_diff_phil=True)

    datablocks = flatten_datablocks(params.input.datablock)

    print "Hi tst"

    if len(datablocks) > 0:
        assert(len(datablocks) == 1)
        imagesets = datablocks[0].extract_imagesets()
        crystals = None
        print "len(datablocks) > 0"

    else:
        raise RuntimeError("No imageset could be constructed")


    '''
    from dials.util.spotfinder_wrap import spot_wrapper

    wrapper = spot_wrapper(params)
    #wrapper.display(imagesets=imagesets, crystals = None)

    img_n5 = wrapper.load_image(5) # wrong way

    print dir(wrapper)
    '''
    print "len(imagesets) =", len(imagesets)
    print "type(imagesets) =", type(imagesets)

    first_data = imagesets[0]

    print "type(first_data) =", type(first_data)
    dir_first_data = '''
    '__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__',
    '__getattribute__', '__getitem__', '__hash__', '__init__', '__iter__',
    '__len__', '__module__', '__new__', '__reduce__', '__reduce_ex__',
    '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
    '__weakref__', '_beam', '_detector', '_get_data_range', '_goniometer',
    '_image_index', '_indices', '_models', '_reader', '_scan', '_to_array_all',
    '_to_array_w_range', '_truncate_range', 'complete_set', 'external_lookup',
    'get_array_range', 'get_beam', 'get_corrected_data', 'get_detector',
    'get_detectorbase', 'get_gain', 'get_goniometer', 'get_image_identifier',
    'get_image_models', 'get_image_size', 'get_mask', 'get_path', 'get_pedestal',
    'get_raw_data', 'get_scan', 'get_template', 'image_cache', 'indices',
    'is_valid', 'paths', 'reader', 'set_beam', 'set_detector', 'set_goniometer',
    'set_scan', 'to_array']'''

    #type(first_data) = <class 'dxtbx.imageset.ImageSweep'>

    print "Trying to_array()"
    my_array = first_data.to_array()
    print "Done to_array()"
    print "type(my_array) =", type(my_array)
