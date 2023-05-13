#include <iostream>
using namespace std;

/*Design a structure named Employee to print the details
of the employee who have 5 years or more experience and 
salary less than 1lac using array of structures 
(Name, ID , experience and salary as member)
Take 3 employees information*/

struct employee
{
	char Emp_name[10];
	int Emp_ID;
	int Emp_experience;
	int Emp_salary;
} 

Emp[3];

int main()
{
	cout << "This is employee information database." << endl;
	for (int i = 0; i < 3; i++)
	{
		cout << endl << "Enter the employee's name: ";
		cin >> Emp[i].Emp_name;
		cout << "Enter the employee's ID: ";
		cin >> Emp[i].Emp_ID;
		cout<< "Enter the employee's experience: ";
		cin >> Emp[i].Emp_experience;
		cout<< "Enter the employee's salary: ";
		cin >> Emp[i].Emp_salary;
	}

	cout << endl << "Please verify the entered information." << endl;

	for (int i = 0; i < 3; i++)
	{
		if (Emp[i].Emp_experience >= 5 && Emp[i].Emp_salary < 100000)
		{
			cout << endl << "Name: " << Emp[i].Emp_name;
			cout << endl << "ID: " << Emp[i].Emp_ID;
			cout << endl << "Experience:" << Emp[i].Emp_experience;
			cout << endl << "Salary: " << Emp[i].Emp_salary << endl;
		}
		
	}
}