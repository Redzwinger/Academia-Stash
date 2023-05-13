#include <iostream>
using namespace std;

struct student
{
	char name[10];
	int sap;
	int marks;
} 

s[3];

int main()
{
	cout << "This is students information" << endl;
	for (int i = 0; i < 2; i++) // input
	{
		cout << "Enter the name " << endl;
		cin >> s[i].name;
		cout << "Enter the sap number " << endl;
		cin >> s[i].sap;
		cout << "Enter the marks " << endl;
		cin >> s[i].marks;
	}

	cout << endl << "......... Display........" << endl;

	for (int i = 0; i < 2; i++) // input
	{
		cout << "name " << s[i].name << endl;
		cout << "sap number " << s[i].sap << endl;
		cout << "marks " << s[i].marks << endl;
	}
}