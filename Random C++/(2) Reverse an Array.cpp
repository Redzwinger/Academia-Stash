#include <iostream>
using namespace std;

int main()
{
    int X[] = { 20,40,60,80,100,120 };
    int Y[6];
    for (int a = 5; a >= 0; a--)
    {
        int c = 5 - a;
        Y[c] = X[a];
    }

    cout << "Reverse of the Original Matrix is: " << endl;

    for (int i = 0; i <= 5; i++)
    {
        cout << Y[i] << " ";
    }
    return 0;
}