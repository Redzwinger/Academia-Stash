#include <iostream>
using namespace std;

int main()
{
    int  a, b;
    int Arr_1[2][3];
    int Arr_2[2][3];
    int Arr_3[2][3];

    cout << "Enter elements for the First Matrix of order 2*3 :" << endl;

    for (a = 0; a < 2; a++)
    {
        for (b = 0; b < 3; b++)
        {
            cout << "Enter element for First Matrix " << a << " " << b << " : ";
            cin >> Arr_1[a][b];
        }
    }
    
    cout << "Enter elements for the Second Matrix of order 2*3 :" << endl;

    for (a = 0; a < 2; a++)
    {
        for (b = 0; b < 3; b++)
        {
            cout << "Enter element Second Matrix " << a << " " << b << " : ";
            cin >> Arr_2[a][b];
        }
    }

    for (a = 0; a < 2; a++)
    {
        for (b = 0; b < 3; b++)
        {
            Arr_3[a][b] = Arr_1[a][b] + Arr_2[a][b];
        }
    }

    cout << endl << "Sum of the two Multi-dimensional Arrays is: " << endl;
    for (a = 0; a < 2; a++)
    {
        for (b = 0; b < 3; b++)
        {
            cout << Arr_3[a][b] << " ";
            if (b == 3 - 1)
                cout << endl;
        }
    }
    return 0;
}