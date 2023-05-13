#include <iostream>
using namespace std;

/*Declare a structure to store the following information about a student:
a. Student code
b. Student name
c. Marks
d. Department number (1-IT, 2-COMP, 3-EXTC, 4-Data Science)*/

struct Info
{
	char stu_name[100];
	float stu_code;
	int stu_marks;
	int stu_dept;
};


int main()
{
	Info Inf1;

	cout << "Enter Student Code: " << endl;
	cin >> Inf1.stu_code;
	cout << "Enter Student Name: " << endl;
	cin >> Inf1.stu_name;
	cout << "Enter Student Marks: " << endl;
	cin >> Inf1.stu_marks;
	cout << "The Department numbers are 1-IT, 2-COMP, 3-EXTC, 4-Data Science" << endl;
	cout << "Enter Student Department Number: " << endl;
	cin >> Inf1.stu_dept;
	

	cout << endl << "Displaying Student Information." << endl;
	cout << "The Student's Code is: " << Inf1.stu_code << endl;
	cout << "The Student's Name is: " << Inf1.stu_name << endl;
	cout << "The Student's Marks are: " << Inf1.stu_marks << endl;
	if(Inf1.stu_dept == 1)
	{
		cout << "The Student's Department is IT." << endl;
	}
	else if (Inf1.stu_dept == 2)
	{
		cout << "The Student's Department is COMP." << endl;
	}
	else if (Inf1.stu_dept == 3)
	{
		cout << "The Student's Department is EXTC." << endl;
	}
	else if (Inf1.stu_dept == 4)
	{
		cout << "The Student's Department is Data Science." << endl;
	}
}