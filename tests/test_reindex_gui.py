import json

import pytest

from dui.dynamic_reindex_gui import MyReindexOpts


@pytest.fixture
def bravais(tmp_path):
    class BravaisFixture:
        def write_summary(self, nitems=8, nrecommended=5):
            # Make a fake reindex data and refine_bravais log
            summary_data = {
                str(x): {
                    "max_angular_difference": 0.0,
                    "rmsd": 0.4242,
                    "nspots": 1000,
                    "bravais": "aP",
                    "unit_cell": [60, 60, 60, 90, 90, 99],
                    "cb_op": "a,b,c",
                    "max_cc": None,
                    "min_cc": None,
                    "correlation_coefficients": [1.0],
                    "cc_nrefs": [1337],
                    "recommended": x <= nrecommended,
                }
                for x in range(nitems)
            }
            summaryjson = tmp_path / "lin_x_bravais_summary.json"
            summaryjson.write_text(json.dumps(summary_data))
            return summaryjson

        def write_log(self, node_id=1):
            log = tmp_path / f"{node_id}_refine_bravais_settings.log"
            log.write_text(
                """Chiral space groups corresponding to each Bravais lattice:
 aP: P1
 mP: P2 P21
 mC: C2
 oRl: -C424242
 ----
"""
            )
            return tmp_path

    return BravaisFixture()


@pytest.fixture
def bravais_summary(bravais):
    def _(*args, **kwargs):
        bravais.write_log(1)
        return bravais.write_summary(*args, **kwargs)

    return _


def test_reindex(bravais_summary, screenshots):
    dialog = MyReindexOpts(None, bravais_summary(nitems=8), 1)
    dialog.show()
    screenshots.saveWindow(dialog)


def test_reindex_many_items(bravais_summary, screenshots):
    dialog = MyReindexOpts(
        None, bravais_summary(nitems=20, nrecommended=3), 1, show_cancel=True
    )
    dialog.show()
    assert dialog.size().height() < 600
    screenshots.saveWindow(dialog)
