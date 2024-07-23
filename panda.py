import pandas

shape_list = ["cube", "cuboid", "sphere", "cylinder", "square pyramid"]
volume_list = [125, 52, 45, 57, 97]
surface_area_list = [187, 97, 98, 164, 132]


sa_v_dict = {
    "Shape": shape_list,
    "Volume": volume_list,
    "Surface Area": surface_area_list
}

sa_v_frame = pandas.DataFrame(sa_v_dict)

sa_v_frame = sa_v_frame.set_index("Shape")

print(sa_v_frame)
