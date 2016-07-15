from dxtbx.datablock import DataBlockFactory
datablocks = DataBlockFactory.from_json_file("datablock.json")

datablocks[0]
db=datablocks[0]

#det=db.unique_detectors()

#det=det[0]

#pnl=det[0]

#pnl.get_raw_data

#db.extract_sweeps()
sw=db.extract_sweeps()[0]

sw.get_raw_data()

sw.get_raw_data(1)
sw.get_raw_data(2)
sw.get_raw_data(0)
im1=sw.get_raw_data(0)[0]
#im1
#im1.all()

