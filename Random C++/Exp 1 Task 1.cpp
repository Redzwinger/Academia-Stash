#include <iostream>
using namespace std;

/*A click counter is a small hand-held device that contains a push button and a count display.
To increment the counter, the button is pushed and the new count shows in the display.
Clicker counters also contain a button that can be pressed to reset the counter to zero.
Design and implement the Counter ADT that functions as a hand-held clicker.*/

class click_counter
{
	int count=0;

public:

	click_counter()
	{
		cout << "Please enter the value of count: ";
		cin >> count;
		cout << endl;
	}
	void push()
	{
		count = count + 1;
		cout << "The count has increased by 1" << endl;
		cout << endl;
	}
	void reset()
	{
		count = 0;
		cout << "The count has been reset to 0." << endl;
		cout << endl;
	}
	void display()
	{
		cout << "The current count is " << count << endl;
		cout << endl;
	}
};

int main()
{
	int choice;
	click_counter c1;

	do
	{
		cout << "1. Push" << endl;
		cout << "2. Reset to Zero" << endl;
		cout << "3. Display the Count" << endl;
		cout << "4. Exit" << endl << " " << endl;

		cout << "Please enter the number of your desired operation: ";
		cin >> choice;
		cout << endl;

		switch (choice)
		{
		case 1:
			c1.push();
			break;

		case 2:
			c1.reset();
			break;

		case 3:
			c1.display();
			break;
		}		
	}
	while (choice != 4);
}