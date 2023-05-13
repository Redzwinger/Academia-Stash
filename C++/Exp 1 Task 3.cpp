#include <iostream>
#include <cstring>
using namespace std;

struct studt_info
{
    int roll_num;
    char grade;
    string name;
};

int main()
{
    int stu;

    cout << "Please enter the number of students: ";    
    cin >> stu;

    studt_info studt[stu];

    for (int i = 0, studt_info = 1; i < stu; i++, studt_info++)
    {
        cout << endl << "Please enter student #" << studt_info << " information:" << endl;
        cout << "Roll number: ";
        cin >> studt[i].roll_num;

        cout << "Name: ";
        cin >> studt[i].name;
        
        cout << "Grade: ";
        cin >> studt[i].grade;
    }

    int choice;
    int search = 0;

    cout << endl << "Do you wish to search by Roll no. [1] or by Name [2] ?" << endl;    
    cin >> choice;

    switch (choice)
    {
    case 1:
    {
        int search_roll_num;
        
        cout << "Please enter the student's Roll number: ";
        cin >> search_roll_num;

        for (int i = 0; i < stu; i++)
        {
            if (studt[i].roll_num == search_roll_num)
            {
                cout << endl << "Record found!" << endl;

                search++;

                cout << "Roll no.: " << studt[i].roll_num << endl;
                cout << "Name: " << studt[i].name << endl;
                cout << "Grade: " << studt[i].grade << endl;
            }
        }

        if (search == 0)
        {
            cout << "Record not found!" << endl;
        }

    }
    break;

    case 2:
    {
        string search_name;

        cout << "Please enter the student's Name: ";        
        cin >> search_name;

        for (int i = 0; i < stu; i++)
        {
            string value = studt[i].name;

            if (value == search_name)
            {
                cout << endl << "Record found!" << endl;

                search++;

                cout << "Roll no.: " << studt[i].roll_num << endl;
                cout << "Name: " << studt[i].name << endl;
                cout << "Grade: " << studt[i].grade << endl;
            }
        }

        if (search == 0)
        {
            cout << "Record not found!" << endl;
        }
    }

    break;

    default:cout << "Please enter a valid option." << endl;
    }
    return 0;
}
    