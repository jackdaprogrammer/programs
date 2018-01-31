//Jack Hosier, Java Variables Learning Part 2

class ReassigningVariables { 
  public static void main ( String[] args ) { 
    double xOne = 0.0;
    double xTwo = 2.0;
    double xThree = 4.0;
    
    double equationOne = (3 * Math.pow(xOne, 2)) - (8 * xOne) + 4;
    double equationTwo = (3 * Math.pow(xTwo, 2)) - (8 * xTwo) + 4;
    double equationThree = (3 * Math.pow(xThree, 2)) - (8 * xThree) + 4;
    
    System.out.println(equationOne);
    System.out.println(equationTwo);
    System.out.println(equationThree);
    
  }
}



