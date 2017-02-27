#include<boost/python.hpp>
#include <iostream>

char const* greet()
{
    return "hello, world";
}

int give_int()
{
    return 5;
}

boost::python::list square(boost::python::list num_lst)
{
    boost::python::list points;
    int one = 1;
    int two = 2;
    int three = 3;
    points.append(one);
    points.append(two);
    points.append(three);
    points.append(num_lst);
    return points;
}

BOOST_PYTHON_MODULE(lst_ext)
{
    using namespace boost::python;
    def("greet", greet);
    def("give_int", give_int);

    def("square", square);
}
