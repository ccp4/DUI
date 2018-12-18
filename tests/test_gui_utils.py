from __future__ import unicode_literals

from dui.gui_utils import get_import_run_string


def test_import_run_string():
    test_inp = [
        "/Users/nickd/dials/data/betalactamase/C2sum_1_0001.cbf.gz",
        "/Users/nickd/dials/data/betalactamase/C2sum_1_0002.cbf.gz",
        "/Users/nickd/dials/data/betalactamase/C2sum_1_0003.cbf.gz",
        "/Users/nickd/dials/data/betalactamase/C2sum_1_0004.cbf.gz",
        "/Users/nickd/dials/data/betalactamase/C2sum_1_0005.cbf.gz",
        "/Users/nickd/dials/data/betalactamase/C2sum_1_0006.cbf.gz",
        "/Users/nickd/dials/data/betalactamase/C2sum_1_0007.cbf.gz",
        "/Users/nickd/dials/data/betalactamase/C2sum_1_0008.cbf.gz",
        "/Users/nickd/dials/data/betalactamase/C2sum_1_0009.cbf.gz",
        "/Users/nickd/dials/data/betalactamase/C2sum_1_0010.cbf.gz",
    ]
    dirname, outs = get_import_run_string(test_inp)
    assert dirname == "/Users/nickd/dials/data/betalactamase"
    assert "image_range=1,10" in outs
    assert "C2sum_1_*.cbf.gz" in outs
    assert "/Users/nickd/dials/data/betalactamase/C2sum_1_" in outs
