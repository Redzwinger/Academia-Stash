#include <iostream>
using namespace std;

/*There are 50 computers in an office.
Every computer has following information CPU type,
hard disk size, keyboard type, mouse type, monitor type.
WAP to store details of all 50 computers and then print details of
computers having hard disk size greater than 8 GB.*/

struct computer
{
	char CPU_Type[100];
	int HDD_size;
	char KeyB_Type[100];
	char Mouse_Type[100];
	char Moniter_Type[100];
}

computer[50];

int main()
{
	cout << "This is a Computer Specifications Database." << endl;
	for (int i = 0; i < 51; i++)
	{
		cout << endl << "Enter the CPU type: ";
		cin >> computer[i].CPU_Type;
		cout << "Enter the HDD size: ";
		cin >> computer[i].HDD_size;
		cout << "Enter the Keyboard type: ";
		cin >> computer[i].KeyB_Type;
		cout << "Enter the Mouse type: ";
		cin >> computer[i].Mouse_Type;
		cout << "Enter the Moniter type: ";
		cin >> computer[i].Moniter_Type;
	}

	cout << endl << "Please verify the entered information." << endl;

	for (int i = 0; i < 51; i++)
	{
		if (computer[i].HDD_size >=8)
		{
			cout << endl << "CPU: " << computer[i].CPU_Type;
			cout << endl << "HDD: " << computer[i].HDD_size;
			cout << endl << "Keyboard:" << computer[i].KeyB_Type;
			cout << endl << "Mouse: " << computer[i].Mouse_Type;
			cout << endl << "Moniter: " << computer[i].Moniter_Type << endl;
		}
		
	}
}