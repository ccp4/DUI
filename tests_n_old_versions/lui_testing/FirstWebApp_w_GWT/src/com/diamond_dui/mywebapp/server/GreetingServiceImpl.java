package com.diamond_dui.mywebapp.server;

import com.diamond_dui.mywebapp.client.GreetingService;
import com.diamond_dui.mywebapp.shared.FieldVerifier;
import com.google.gwt.user.server.rpc.RemoteServiceServlet;

import java.io.*;

/**
 * The server-side implementation of the RPC service.
 */
@SuppressWarnings("serial")
public class GreetingServiceImpl extends RemoteServiceServlet implements
    GreetingService {

  public String greetServer(String input) throws IllegalArgumentException {
    // Verify that the input is valid.
    if (!FieldVerifier.isValidName(input)) {
      // If the input is not valid, throw an IllegalArgumentException back to
      // the client.
      throw new IllegalArgumentException(
          "command must be at least 2 characters long");
    }
    ////////////////////////////////////////////////////
    // Here is the code that will run from the server  /
    ////////////////////////////////////////////////////



    System.out.println("Here from server ");
    System.out.println("Entered " + input);




    String s = null;
    try {

      // using the Runtime exec method:
      Process p = Runtime.getRuntime().exec(input);

      BufferedReader stdInput = new BufferedReader(new
           InputStreamReader(p.getInputStream()));

      // read the output from the command
      System.out.println("Running CLI:\n");
      while ((s = stdInput.readLine()) != null) {
          System.out.println(s);
      }

      //System.exit(0);
    }
    catch (IOException e) {
      System.out.println("exception happened");
      //System.exit(-1);
    }



    String serverInfo = getServletContext().getServerInfo();
    String userAgent = getThreadLocalRequest().getHeader("User-Agent");

    // Escape data from the client to avoid cross-site script vulnerabilities.
    input = escapeHtml(input);
    userAgent = escapeHtml(userAgent);

    return "Hello, " + input + "!<br><br>I am running " + serverInfo
        + ".<br><br>It looks like you are using:<br>" + userAgent;
  }

  /**
   * Escape an html string. Escaping data received from the client helps to
   * prevent cross-site script vulnerabilities.
   *
   * @param html the html string to escape
   * @return the escaped string
   */
  private String escapeHtml(String html) {
    if (html == null) {
      return null;
    }
    return html.replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(
        ">", "&gt;");
  }
}
