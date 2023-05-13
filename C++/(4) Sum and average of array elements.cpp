#include <iostream>
using namespace std;

int main()
{
    int sum = 0, length;
    float avg;

    int num[7] = { 4,6,8,9,10,12,14 };

    //if numbers are to be taken from the user
    /*
    cout << "Enter seven numbers: " << endl;

    for (int i = 0; i < 7; i++)
    {
        cin >> num[i];
    }
    */

    for (int i = 0; i < 7; i++)
    {
        sum = sum + num[i];
    }

    cout << "The sum of the numbers is: " << sum << endl;

    length = sizeof(num) / sizeof(num[0]);
    avg = sum / length;

    cout << "The average of the numbers is: " << avg << endl;
    return 0;
}