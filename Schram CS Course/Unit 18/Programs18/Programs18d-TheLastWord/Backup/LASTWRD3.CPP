// LASTWRD3.CPP
// This program will count backwards from 20 to 0.
// For each number, it will display whether it has 1 or 2 digits.
// Compare this C++ code to the code from other languages.

#include <iostream.h>
#include <conio.h>

void main()
{
   for (int k = 20; k >= 0; k--)
   {
		if (k >= 10)
		{
	    	cout << k << " is a 2-digit number." << endl;
		}
		else
		{
	    	cout << j << " is a 1-digit number." << endl;
		}
   }
   cout << endl;
   getch();  // makes the computer wait until a character is pressed
}
