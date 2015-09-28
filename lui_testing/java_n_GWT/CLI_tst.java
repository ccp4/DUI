import java.io.*;

class CLI_tst {

  public static void main(String args[]) {

    String s = null;
    try {

      // using the Runtime exec method:
      Process p = Runtime.getRuntime().exec("dials.import");

      BufferedReader stdInput = new BufferedReader(new
           InputStreamReader(p.getInputStream()));

      // read the output from the command
      System.out.println("Running CLI:\n");
      while ((s = stdInput.readLine()) != null) {
          System.out.println(s);
      }

      System.exit(0);
    }
    catch (IOException e) {
      System.out.println("exception happened");
      System.exit(-1);
    }
  }

}
