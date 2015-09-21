/**
 * My first exercise in Java.
 */
class cuadratic_function {

    private double d = -99999999.99999999;
    private double a = 0;
    private double b = 0;
    private double c = 0;
    private int n_resp = 0;

    public cuadratic_function(double in_a, double in_b, double in_c){
        System.out.println("Entered (a, b, c) = (" + in_a +
                           ", " + in_b + ", " + in_c + " )");
        a = in_a;
        b = in_b;
        c = in_c;

        d = b * b - 4 * a * c;
        if( d > 0 ){
          n_resp = 2;
        } else if( d == 0)  {
          n_resp = 1;
        } else {
          n_resp = 0;
        }
    }

    public double get_D(){
        return this.d;
    }

    public double[] get_x1_x2(){
        double[] local_x1_x2;
        local_x1_x2 = new double[2];

        if( d > 0 ){
            local_x1_x2[0] = (-b + Math.sqrt(d) ) / ( 2 * a );
            local_x1_x2[1] = (-b - Math.sqrt(d) ) / ( 2 * a );
        } else if( d == 0)  {
            local_x1_x2[0] = (-b ) / ( 2 * a );
            local_x1_x2[1] = -99999999.99999999;
        } else {
            local_x1_x2[0] = -99999999.99999999;
            local_x1_x2[1] = -99999999.99999999;
        }

        return local_x1_x2;
    }

    public int print_result(){
        if( d > 0 || n_resp == 2 ){
          System.out.println("There are 2 solutions");
        } else if( d == 0 || n_resp == 1 )  {
          System.out.println("There is one solution");
        } else {
          System.out.println("no solution D < 0");
        }
        return 0;
    }

}

class MainApp {
    public static void main(String[] args) {
        System.out.println("Cuadratic function");
        cuadratic_function func_1 = new cuadratic_function(2, -3, 1);
        //cuadratic_function func_1 = new cuadratic_function(1, 2, 3);
        System.out.println("D(call)  = " + func_1.get_D());
        double[] main_x1_x2;
        int nr = 0;
        main_x1_x2 = new double[2];
        main_x1_x2 = func_1.get_x1_x2();
        System.out.println("x1, x2  = " + main_x1_x2[0] +
                           " ,  " + main_x1_x2[1]);

        //func_1.print_result();

    }
}
