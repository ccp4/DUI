/**
 * My first exercise in Java.
 */
class calc_class {

    private double d = -1;
    private double a = 0;
    private double b = 0;
    private double c = 0;

    public calc_class(double in_a, double in_b, double in_c){
        System.out.println("Entered (a, b, c) = (" + in_a +
                           ", " + in_b + ", " + in_c + " )");
        a = in_a;
        b = in_b;
        c = in_c;

        d = b * b - 4 * a * c;
        System.out.println("D = " + d);
    }

    public double get_D(){
        return this.d;
    }

    public double[] get_x1_x2(){
        double[] local_x1_x2;
        local_x1_x2 = new double[2];
        local_x1_x2[0] = (-b + Math.sqrt(d) ) / ( 2 * a );
        local_x1_x2[1] = (-b - Math.sqrt(d) ) / ( 2 * a );
        return local_x1_x2;
    }
}

class MainApp {
    public static void main(String[] args) {
        System.out.println("Cuadratic function");
        calc_class func_1 = new calc_class(2, 3, 1);
        System.out.println("D(call)  = " + func_1.get_D());
        double[] main_x1_x2;
        main_x1_x2 = new double[2];
        main_x1_x2 = func_1.get_x1_x2();
        System.out.println("x1, x2  = " + main_x1_x2[0] +
                           " ,  " + main_x1_x2[1]);
    }
}
