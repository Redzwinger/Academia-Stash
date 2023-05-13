#include <iostream>
using namespace std;

/*ADT of Queue (enqueue/insert, dequeue/delete)*/

#define size 5

int frnt = -1;
int rer = -1;
int kqu[size]; //Queue

void enkqu()        //Inserting an element
{
    int o;

    cout << endl << "Please enter the number that is to be inserted into the Queue: ";
    cin >> o;

    if ((rer + 1) % size == frnt)
    {
        cout << endl << "Error! Queue Overflow!" << endl;
    }
    else if (rer == -1 && frnt == -1)
    {
        frnt = rer = 0;
        kqu[rer] = o;
    }
    else
    {
        rer = (rer + 1) % size;
    }

    kqu[rer] = o;

    cout << endl << "The element " << o << " has been inserted into the Queue." << endl;
}

void dekqu()      //Deleting an element
{
    int g;

    if (frnt == -1 && rer == -1)
    {
        cout << endl << "Error! Queue Underflow!" << endl;
    }
    else if (frnt == rer)
    {
        frnt = rer = -1;
    }
    else
    {
        frnt = (frnt + 1) % size;
        cout << endl << "The element " << g << " has been deleted." << endl;
    }
}

void display()    //Displaying the Queue
{
    if (frnt > rer || frnt == -1)
    {
        cout << endl << "The Queue is Empty." << endl << "(Error! Queue Underflow!)" << endl;
    }
    else
    {
        cout << endl << "The current Queue is:";

        for (int h = frnt; h <= rer; h++)
        {
            cout << " " << kqu[h] << " " << endl;
        }
    }
}

int main()
{
    int TheChosenSelection;

    cout << "This program does the following operations on a Queue:" << endl << "(Note: By default the Queue is empty.)" << endl;

    do
    {
        cout << endl << "1. Enqueue (Inserting an element)" << endl;
        cout << "2. Dequeue (Deleting an element)" << endl;
        cout << "3. Display (Displaying the entire Queue)" << endl;
        cout << "4. Exit (Terminating the program)" << endl;
        cout << endl << "Please enter the number preceeding the desired operation: ";
        cin >> TheChosenSelection;

        switch (TheChosenSelection)
        {
        case 1:
            enkqu();
            break;

        case 2:
            dekqu();
            break;

        case 3:
            display();
            break;

        case 4:
            cout << endl << "Program Terminated..." << endl;
            break;

        default:
            cout << endl << " Invalid Choice." << endl;
        }
    } 
    while (TheChosenSelection != 4);
}