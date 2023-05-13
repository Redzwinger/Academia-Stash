#include <iostream>
using namespace std;

int main() 
{
    int num[5];
    cout << "Enter 5 numbers: " << endl;

    for (int i = 0; i < 5; ++i)
    {
        cin >> num[i];
    }

    cout << "The Numbers are:";

    for (int i = 0; i < 5; ++i)
    {
        cout << " " << num[i];
    }
    return 0;
}