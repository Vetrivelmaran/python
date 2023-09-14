import java.util.Scanner;

public class New{
	public static void main(String[] arg){
System.out.println("hello world");
try (Scanner sc = new Scanner(System.in)) {
	int a = sc.nextInt();
	
	
	int b = sc.nextInt();
	
	System.out.println(a+b);
}


}}