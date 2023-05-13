#include <iostream>
using namespace std;

     /*Problem Statement:
	  Write a program to calculate the salary of the person with the following allowance.
	  DA = 28 % of basic
	  HRA = 30 % of basic
	  TA = 2000 INR
	  Write a function to calculate the salary. Take the basic pay from the user.*/

float salary_calculator (int basic_salary)
{
	int TA;
	float DA, HRA, salary_plus_allowances;

	TA = 2000;
	DA = basic_salary * 0.28;
    HRA = basic_salary * 0.30;

	salary_plus_allowances = basic_salary + DA + HRA + TA;
	return salary_plus_allowances;
}

int main()
{
	int user_salary;
	float total_salary;

	cout << "This a Salary Calculator Program." << endl;
	cout << "This program will calculate the total salary of the user based on the entered basic salary" << endl;
	cout << "Please enter your basic salary: ";

	cin >> user_salary;
	total_salary = salary_calculator(user_salary);

	cout << "Total Salary is calculated as basic salary (" << user_salary << ") + allowances (DA + HRA + TA)" << endl;
	cout << "Total salary of the current user is INR " << total_salary << "/-";
}