#include<boost/python.hpp>
#include <iostream>

namespace py = boost::python;

char const* greet()
{
    return "hello, world";
}

int give_int()
{
    return 5;
}

py::list square(py::list num_lst)
{
    /*
     * This example shows how to input a python list
     * and plays a bit with it
     */
    py::list points;
    int one = 1;
    int two = 2;
    int three = 3;
    points.append(one);
    points.append(two);
    points.append(three);
    points.append(num_lst);
    return points;
}

py::list arange_list(py::list bbox_lst, int n_imgs)
{
    /*
     * This is the function that we actually need.
     *
     * from a list of shoe - box bounds
     * it generates a new list of reflections arranged
     * per image
     */
    std::cout << "n_imgs =" << n_imgs << "\n";

    /*
     * Translating:
     *
            for i in xrange(n_refs):
                local_bbox = table[i]['bbox']
                z_boud = local_bbox[4:6]
                x_ini = local_bbox[0]
                y_ini = local_bbox[2]
                width = local_bbox[1] - local_bbox[0]
                height = local_bbox[3] - local_bbox[2]


                for idx in xrange( int(z_boud[0]), int(z_boud[1]) ):
                    reflection_data = flat_data()
                    reflection_data.box = [x_ini, y_ini, width, height]
    */

    int x_ini, y_ini, width, height;
    py::list img_lst, ref_box, empty_lst;

    //TODO make sure there is no way to avoid this loop
    for (int i = 0; i < n_imgs; i++){
        img_lst.append(empty_lst);
    }

    for (int i = 0; i < len(bbox_lst); i++){
        ref_box = py::extract<py::list>(bbox_lst[i]);
        x_ini = py::extract<int>(ref_box[0]);
        y_ini = py::extract<int>(ref_box[2]);
        width = py::extract<int>(ref_box[1]) - py::extract<int>(ref_box[0]);
        height = py::extract<int>(ref_box[3]) - py::extract<int>(ref_box[2]);
        /*
        empty_lst.clear();
        empty_lst.append(x_ini);
        empty_lst.append(y_ini);
        empty_lst.append(width);
        empty_lst.append(height);
        */
        for (int idx = py::extract<int>(ref_box[4]);
             idx < py::extract<int>(ref_box[5]);
             idx++){
            std::cout << "limits =" << x_ini << ", " << y_ini << ", " <<
                      width << ", " << height << "\n" << "idx[n] = " <<
                       idx << "\n";
            //py::extract<py::list>(img_lst[idx]).append(ref_box);
        }
    }

    //img_lst[1] = bbox_lst[2];


    return img_lst;
}
BOOST_PYTHON_MODULE(lst_ext)
{
    using namespace boost::python;
    def("greet", greet);
    def("give_int", give_int);
    def("square", square);
    def("arange_list", arange_list, arg("bbox_lst"), arg("n_imgs"));
    //def("arange_list", &arange_list, arg("bbox_lst"), arg("n_imgs"));


}
