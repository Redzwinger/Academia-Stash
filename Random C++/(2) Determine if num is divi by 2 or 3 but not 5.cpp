#include <iostream>
using namespace std;

int main()
{
	int num, two, three, five;

	cout << "Enter a number to determine if it is divisible by 2 or 3 but not 5: ";
	cin >> num;

	two = num % 2;
	three = num % 3;
	five = num % 5;

	if (five != 0)
	{
		if ((two == 0) || (three == 0))
		{
			cout << "The entered number is divisible by 2 or 3 but not divisible by 5" << endl;
		}
	}
	else
	{
		cout << "The entered number is divisible by 5 and hence, is invalid" << endl;
	}
	return 0;
}