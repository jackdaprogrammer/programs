//Jack Hosier - Java Learning Variables Part 2

class PayrollProgram { 
  public static void main ( String[] args ) { 
    long hoursWorked;
    hoursWorked= 40; 
    double payRate;
    payRate= 10.0;
    double taxRate;
    taxRate= 0.10; 
    
    System.out.println("Hours Worked: " + hoursWorked ); 
    System.out.println("pay Amount : " + (hoursWorked * payRate) ); 
    System.out.println("tax Amount : " + (hoursWorked * payRate * taxRate) ); 
  }
}
