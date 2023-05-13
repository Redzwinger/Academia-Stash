#include <iostream>
#include <cmath>
using namespace std;

void math()
{

	//Program to calculate the value of the expression y=a^b using void

	int a, b, c;
	cout << "For the expression y=a^b, enter the value of a: ";
	cin >> a;

	cout << endl << "For the expression y=a^b, enter the value of b: ";
	cin >> b;

	c = pow(a, b);

	cout << endl << "The solution of the expression y=a^b for the entered values is: " << c;
}

int main()
{
	math();
}