#include <iostream>
using namespace std;

int main()
{
    int n = 10, placeholder;

    int Arr[10] = { 10,56,84,32,64,51,30,47,21,63 };

    for (int a = 0; a < n; a++)
    {
        for (int b = 1 + a; b < n; b++)
        {
            if (Arr[a] < Arr[b])
            {
                placeholder = Arr[a];
                Arr[a] = Arr[b];
                Arr[b] = placeholder;
            }
        }
    }

    cout << "The Array arranged in Descending order is: ";

    for (int a = 0; a < n; a++)
    {
        cout << Arr[a] << " ";
    }

    return 0;
}