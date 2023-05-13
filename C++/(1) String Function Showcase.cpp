#include <iostream>
#include <cstring>
using namespace std;

int main()
{
	//Program showcasing the string functions strlen(), strcmp(), strcat(), strcpy()

    char words_which_have_meaning[] = "This string showcases the string functions.";

	char words_which_also_have_meaning[] = " This string also showcases the string functions";

	int count = 0;

	//Showcasing the first string function strlen()

	cout << "The length of the string is " << strlen(words_which_have_meaning) << endl;

	//Showcasing the second string function strcmp()

	count = strcmp(words_which_have_meaning, words_which_also_have_meaning);

	cout << "On comparing the first two strings we get: " << count << endl;

	//Showcasing the third string function strcat()

	strcat(words_which_have_meaning, words_which_also_have_meaning);

	cout << words_which_have_meaning << endl;

	//Showcasing the fourth string function strcpy()

	char final_string[] = "This string showcases the last string function";

	char final_output_string[100];

	strcpy(final_output_string, final_string);

	cout << final_output_string << endl;

	return 0;
}





