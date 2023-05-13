#include <iostream>
using namespace std;

/*Accessing array elements using pointers*/

int main()
{
    int arr_tb_accessed[4];
    cout << "Please enter the elements of the array: " << endl;

    for (int i = 0; i < 4; i++)
    {
        cin >> arr_tb_accessed[i];
    }
    cout << "The Entered Array is: " << endl;

    for (int i = 0; i < 4; i++)
    {
        cout << *(arr_tb_accessed + i) << endl;
    }
        
    return 0;
}