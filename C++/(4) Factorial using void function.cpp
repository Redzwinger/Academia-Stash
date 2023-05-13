#include <iostream>
#include <cmath>
using namespace std;

void math(int x)
{
    //Program for calculating the factorial of a number given by the user
    int factorial = 1;

    while (x >= 1)
    {
        factorial *= x;
        --x;
    }

    cout << endl << "The Factorial of the given number is : " << factorial;
}
int main()
{
    int num;
    cout << "Enter the number whose factorial should be calculated: ";
    cin >> num;
    math(num);
}