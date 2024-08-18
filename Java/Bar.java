import java.util.Date;
// use imports to use different already built classes

public class Bar {
  public static void main(String[] args) {
    System.out.println("Bar.java file running...");

    // primitives make a copy another wheras nonprimitives hold references of another

    // new keyword used to allocate space
    Person p1 = new Person("samin");
    System.out.println(p1.name);

    // Strings are multiple characters
    String name = new String("THIS IS A STRING");
    System.out.println(name.toUpperCase()); // converts original string to uppercase
    System.out.println(name);

    // .charAt(index) = returns character at specified index in a string
    Date date = new Date();

    // can't use reserved keywords - class, static, main, etc

    System.out.println(10 * 2);
    System.out.println(10 + 2);
    System.out.println(10 - 2);
    System.out.println(10 % 2);

    // Math.abs()
    // Math.max(list)
    // Math.min
    // Math.pow(base, power)
    // Math.PI

    boolean test = true;
    int age = 18;
    String message = age >= 18 ? ">= 18" : "< 18"; // terniary operator

    if (test == true && age >= 18) {
      System.out.println("valid");
    } else if (test == false && age == 18) {
      System.out.println("HMMMM");
    } else {
      System.out.println("IDK");
    }

    // need to use .equals to compare strings

    // ARRARYS
    int [] numbers = new int[2];
  }

  static class Person {
    String name;
    Person(String name) {
      this.name = name;
    }
  }
}

// https://www.youtube.com/watch?v=Qgl81fPcLc8&t=907s 2:15