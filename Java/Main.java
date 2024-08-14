// use javac file.java to use java compiler --> creates .class which contains byte code --> goes to VM
// javac file.java
// java file.class

// package is way to organize classes

// importing class/library
import java.util.Date;

public class Main {
  public static void main(String[] args) {
    // System.out.println("hello world");

    // primitive and nonprimitive data types
    int number = 100;  // primitive
    double decimal = 100.1;
    String name = "Samin";  // nonprimitive
    Date date = new Date();
    
    // new keyword used to create instance of class
    String last_name = new String("sarker");
    // allocating memory and passing up string to constructor

    System.out.println(last_name);
    System.out.println(last_name.toUpperCase());

  }
}

// https://www.youtube.com/watch?v=Qgl81fPcLc8&t=907s