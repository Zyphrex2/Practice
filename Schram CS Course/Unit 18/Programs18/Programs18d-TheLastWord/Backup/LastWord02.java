// LastWord02.java
// This program will count backwards from 20 to 0.
// For each number, it will display whether it has
// 1 or 2 digits. Compare this Java code to the 
// code from other languages.

public class LastWord02
{
	public static void main (String args[])
	{
   	System.out.println();
		for (int k = 20; k >= 0; k--)
		{
			if (k >= 10)
			{
				System.out.println(k + " is a 2-digit number.");
			}
			else
			{
				System.out.println(k + " is a 1-digit number.");
			}
		}
	}
}
