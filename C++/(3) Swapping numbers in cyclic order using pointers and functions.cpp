#include <iostream>
using namespace std;

/*C++ Program to Swap Numbers in Cyclic Order with pointers AND functions*/

void CyclicSwap(int* p, int* q, int* r) 
{
	int t;
	t = *r;
	*r = *q;
	*q = *p;
	*p = t;
}

int main()
{
	int a, b, c;

	cout << "This program swaps the given numbers in cyclic order." << endl;

	cout << "Please enter the 1st number: ";
	cin >> a;
	cout << "Please enter the 2nd number: ";
	cin >> b;
	cout << "Please enter the 3rd number: ";
	cin >> c;

	cout << "The numbers before swapping are: " << a << ", " << b << ", " << c << endl;

	CyclicSwap(&a, &b, &c); 

	cout << endl << "The numbers after swapping are: ";
	cout << a << ", " << b << ", " << c;
}