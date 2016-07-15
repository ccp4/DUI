from dxtbx.datablock import DataBlockFactory
datablocks = DataBlockFactory.from_json_file("/home/luiso/dui/dui_test/only_9_img/idials_tst_04/dials-1/1_import/datablock.json")

datablocks[0]
db=datablocks[0]

sw=db.extract_sweeps()[0]

print sw.get_raw_data(1)
print sw.get_raw_data(2)
print sw.get_raw_data(0)
im1=sw.get_raw_data(0)[0]

print im1.all()

