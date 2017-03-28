#include<boost/python.hpp>
#include <iostream>

namespace py = boost::python;

char const* greet()
{
    return "hello, world";
}

int find_closer_hkl_func(float x_mouse_scaled, float y_mouse_scaled, py::list flat_data_lst){
    /*
     * finding the closer reflection from an X,Y position in one image
     */

    std::cout << "\n x_mouse_scaled = " << x_mouse_scaled
              << "\n y_mouse_scaled = " << y_mouse_scaled
              << "\n len(flat_data_lst) = " << len(flat_data_lst)
              << "\n";

    return -1;
}

/*
 * This should be redone in C++
def find_closer_hkl_func(x_mouse_scaled, y_mouse_scaled, flat_data_lst):

    dst_squared = 999999.0
    hkl_result = None
    for i, reflection in enumerate(flat_data_lst):
        x = float(reflection[0]) + float(reflection[2]) / 2.0
        y = float(reflection[1]) + float(reflection[3]) / 2.0

        tmp_dst_squared = (x - x_mouse_scaled) ** 2.0 + (y - y_mouse_scaled) ** 2.0

        if( tmp_dst_squared < dst_squared ):
            hkl_result = i
            dst_squared = tmp_dst_squared

    return hkl_result

*/
py::list arrange_list(py::list bbox_lst, py::list hkl_lst, int n_imgs){
    /*
     * from a list of shoe - box bounds and another HKL list
     * it generates a new list with lists on it with reflections arranged
     * per image
     */

    std::cout << "n_imgs =" << n_imgs << "\n";

    int x_ini, y_ini, width, height;
    py::list img_lst, ref_box, tmp_lst, box_dat;

    //TODO make sure there is no way to avoid this loop
    for (int i = 0; i < n_imgs; i++){
        img_lst.append(py::list());
    }
    py::str local_hkl;

    for (int i = 0; i < len(bbox_lst); i++){
        ref_box = py::extract<py::list>(bbox_lst[i]);
        x_ini = py::extract<int>(ref_box[0]);
        y_ini = py::extract<int>(ref_box[2]);
        width = py::extract<int>(ref_box[1]) - py::extract<int>(ref_box[0]);
        height = py::extract<int>(ref_box[3]) - py::extract<int>(ref_box[2]);

        box_dat = py::list();
        box_dat.append(x_ini);
        box_dat.append(y_ini);
        box_dat.append(width);
        box_dat.append(height);


        if( len(hkl_lst) <= 1 ){
            local_hkl = "";
            box_dat.append(local_hkl);
        } else {
            local_hkl = py::extract<py::str>(hkl_lst[i]);
            if(local_hkl == "(0, 0, 0)"){
                local_hkl = "NOT indexed";
            }

            box_dat.append(local_hkl);
        }

        for (int idx = py::extract<int>(ref_box[4]);
             idx < py::extract<int>(ref_box[5]);
             idx++){
            tmp_lst = py::extract<py::list>(img_lst[idx]);
            tmp_lst.append(box_dat);
        }
    }

    return img_lst;
}
BOOST_PYTHON_MODULE(lst_ext)
{
    using namespace boost::python;
    def("greet", greet);
    def("arrange_list", &arrange_list, arg("bbox_lst"), arg("hkl_lst"), arg("n_imgs"));
    def("find_closer_hkl_func", &find_closer_hkl_func, arg("x_mouse_scaled") ,
        arg("y_mouse_scaled"), arg("flat_data_lst"));

}
