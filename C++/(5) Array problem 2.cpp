#include <iostream>
using namespace std;

int main()
{
    int num[4] = { 5,10,15,20 };
    int generic_num = 1;

    for (int a = 0; a < 4; a++)
    {
        cout << num[a] * generic_num << " ";
        ++generic_num;
    }
    return 0;
}