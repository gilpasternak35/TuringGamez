import java.io.File;
import java.lang.ProcessBuilder.Redirect;

/**
 * @author Jesse Steinberg
 * @author Gil Pasternak
 */
public class TuringGamez {

  /**
   * @param args
   */
  public static void main(String[] args) {
    // write your code here
    System.out.println("This will be a controller");

    // Create a controller
    // Run that controller

    /*
     *
     * Testing running a Python script using Process
     *
     */

    try {
      Process script = new ProcessBuilder("python", "py_script.py")
          .directory(new File("C:\\Users\\Jesse\\Documents\\PersonalProjects\\TuringGamez"
              + "\\controller_code\\src\\")).inheritIO()
          .start();
      System.out.print(String.format("Script is alive: %s\n", script.isAlive()));
      System.out.print(String.format("Script pid stream: %s\n", script.pid()));
      System.out.print(String.format("Script input stream: %s\n",
          script.getInputStream().toString()));
      System.out.print(String.format("Script output stream: %s\n",
          script.getOutputStream().toString()));
      script.destroy();
      System.out.print(String.format("Script exit value: %s\n", script.exitValue()));

      System.out.print("It ran?");
    } catch (Exception e) {
      System.out.println("Error: " + e.getMessage());
      e.getStackTrace();
    }

  }
}
