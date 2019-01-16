from __future__ import unicode_literals

import os
import posixpath
import ntpath

from dui.gui_utils import get_import_run_string


def test_import_run_string_posix(monkeypatch):
    monkeypatch.setattr(os, "path", posixpath)
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
    assert "C2sum_1_*.cbf.gz" in outs or "C2sum_1_00*.cbf.gz" in outs
    assert "/Users/nickd/dials/data/betalactamase/C2sum_1_" in outs


def test_import_run_string_windows(monkeypatch):
    monkeypatch.setattr(os, "path", ntpath)
    test_inp = [
        "c:\\Users\\nickd\\dials\\data\\betalactamase\\C2sum_1_0001.cbf.gz",
        "c:\\Users\\nickd\\dials\\data\\betalactamase\\C2sum_1_0002.cbf.gz",
        "c:\\Users\\nickd\\dials\\data\\betalactamase\\C2sum_1_0003.cbf.gz",
        "c:\\Users\\nickd\\dials\\data\\betalactamase\\C2sum_1_0004.cbf.gz",
        "c:\\Users\\nickd\\dials\\data\\betalactamase\\C2sum_1_0005.cbf.gz",
        "c:\\Users\\nickd\\dials\\data\\betalactamase\\C2sum_1_0006.cbf.gz",
        "c:\\Users\\nickd\\dials\\data\\betalactamase\\C2sum_1_0007.cbf.gz",
        "c:\\Users\\nickd\\dials\\data\\betalactamase\\C2sum_1_0008.cbf.gz",
        "c:\\Users\\nickd\\dials\\data\\betalactamase\\C2sum_1_0009.cbf.gz",
        "c:\\Users\\nickd\\dials\\data\\betalactamase\\C2sum_1_0010.cbf.gz",
    ]
    dirname, outs = get_import_run_string(test_inp)
    assert dirname == "c:\\Users\\nickd\\dials\\data\\betalactamase"
    assert "image_range=1,10" in outs
    assert "C2sum_1_*.cbf.gz" in outs or "C2sum_1_00*.cbf.gz" in outs
    assert "c:\\Users\\nickd\\dials\\data\\betalactamase\\C2sum_1_" in outs


def test_import_run_string_other():
    filenames = [
        (["hg_001.mar1600"], "hg_*.mar1600"),
        (["hg_001.bz2"], "hg_*.bz2"),
        (["something_some.h5"], "something_some.h5"),
        (["a.h5", "b.h5"], "a.h5 b.h5"),
        (["a_001.cbf", "another_form_0002.cbf"], "a_001.cbf another_form_0002.cbf"),
    ]
    for input, output in filenames:
        assert get_import_run_string(input)[1] == output
