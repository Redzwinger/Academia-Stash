#include<iostream>
using namespace std;

/*C++ Program to Swap Numbers in Cyclic Order using only pointers*/

int main()
{
    int a, b, c;

    int* x = &a;
    int* y = &b;
    int* z = &c;

    cout << " This program swaps the given numbers in cyclic order." << endl;

    cout << "Please enter the 1st number: ";
    cin >> a;
    cout << "Please enter the 2nd number: ";
    cin >> b;
    cout << "Please enter the 3rd number: ";
    cin >> c;

    cout << "The numbers before swapping are: " << a << ", " << b << ", " << c << endl;

    int temp;
    temp = *z;
    *z = *y;
    *y = *x;
    *x = temp;

    cout << endl << "The numbers after swapping are: ";
    cout << a << ", " << b << ", " << c;
}