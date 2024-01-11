#include <iostream>
using namespace std;

//Write a program to implement Abstract Data Structure of Stack.

#define size 5

int stac[size];
int top = -1;

	int overflow()
	{
		if (top == size - 1)
		{
			cout << "The Stack is full." << endl;
			return (1);
		}
		else
		{
			return (0);
		}
	}

	int underflow()
	{
		if (top == -1)
		{
			cout << "The Stack is empty." << endl;
			return (1);
		}
		else
		{
			return(0);
		}
	}

	void push(int val)
	{
		int a;
		a = overflow();

		if (a == 1)
		{
			return;
		}
		else
		{
			top++;
			stac[top] = val;
		}
	}

	void pop()
	{
		int b, val_2;
		b = underflow();
		
		if (b == 1)
		{
			return;
		}
		else
		{
			val_2 = stac[top];
			cout << "The element " << val_2 << " is deleted." << endl;
			top--;
		}
	}

	void peek()
	{
		if (top <= -1)
		{
			underflow();
		}
		else
		{
			cout << "The topmost element is " << stac[top] << "." << endl;
		}
	}

	void display()
	{
		if (top >= 0)
		{
			cout << "The Stack Elements are: " << endl;

			for (int i = top; i >= 0; i--)
			{
				cout << stac[i] << " ";
				cout << endl;
			}
		}
		else
		{
			underflow();
		}
	}

int main()
{
	int choice, entered_value;

	cout << "1) Push in stack." << endl;
	cout << "2) Pop from stack." << endl;
	cout << "3) Display stack." << endl;
	cout << "4) Peep from stack." << endl;
	cout << "5) Exit." << endl;

	do
	{
		cout << "Enter choice: " << endl;
		cin >> choice;

		switch (choice)
		{
		case 1:
		{
			cout << "Please enter the value to be pushed:" << endl;
			cin >> entered_value;
			push(entered_value);
			break;
		}
		case 2:
		{
			pop();
			break;
		}
		case 3:
		{
			display();
			break;
		}
		case 4:
		{
			peek();
			break;
		}
		case 5:
		{
			cout << "Program Terminated..." << endl;
			break;
		}
		default:
		{
			cout << "Invalid Choice" << endl;
		}
		}
	}
	while (choice != 5);
	return 0;
}
