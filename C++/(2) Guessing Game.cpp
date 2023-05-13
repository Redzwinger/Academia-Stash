#include <iostream>
using namespace std;

int main()
{
	char correct_answer[] = "Cheese";
	char guess[100];
	char replayability = 'Y';
	int attempts = 1;
	cout << endl << "\t\t \t    Welcome!" << endl << "\t\t This is a guessing game called" << endl << "\t\t \tGuess The Answer!" << endl;
	cout << "\tYou will have FIVE chances to guess the correct answer" << endl << "\t\t \t   Good Luck!" << endl << endl;
	while (replayability == 'Y')
	{
		if (attempts <= 5)
		{
			cout << endl << "\t Guess #" << attempts << ": ";
			cin >> guess;
			if (strcmp(guess, correct_answer) == 0)
			{
				cout << endl << "\t WHOOO HOOO!!! You have guessed the correct answer :D " << endl;
				cout << "\t You guessed correctly in " << attempts << " attempts." << endl;
				cout << "\t To replay enter Y" << endl;
				cin >> replayability;
				attempts = 1;
			}
			else
			{
				cout << "\t Whoops! You guessed incorrectly!" << endl;
				cout << "\t No worries, give it another shot! ;)" << endl << endl;
				++attempts;
			}
		}
		else
		{
			cout << "\t Uh Oh! You have run of attempts!" << endl;
			cout << "\t Do you wish to restart? [Y/N] : ";
			cin >> replayability;
			attempts = 1;
		}
	}
}