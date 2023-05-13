#include <iostream>
using namespace std;

int main() {
    int Year;

    cout << "Enter year that is to be identified: ";
    cin >> Year;

    if (Year % 4 == 0)
    {
        if (Year % 100 == 0)
        {
            if (Year % 400 == 0)
            {
                cout << "The year " << Year << " is a leap year." << endl;
            }
            else
            {
                cout << "The year " << Year << " is not a leap year." << endl;
            }
        }
        else
        {
            cout << "The year " << Year << " is a leap year." << endl;
        }
    }
    else
    {
        cout << "The year " << Year << " is not a leap year." << endl;
    }
    return 0;
}