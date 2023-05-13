#include <iostream>
using namespace std;

struct node
{
	int data;
	struct node* next;
};

struct node* head = NULL;

void insert_beginning()
{
	int d;
	struct node* temp; //address of node

	temp = new(struct node);
	cout << endl << "Enter data to be inserted in the beginning of the linked list: ";
	cin >> d;

	temp->data = d;
	temp->next = NULL;

	if (head == NULL) /*if list is empty*/
	{
		head = temp;
		return;
	}
	else //if list is not empty
	{
		temp->next = head;
		head = temp;
	}
}

void insert_end()
{
	struct node* n = new node;
	struct node* current;
	int v;
	cout << endl << "Enter data to be inserted at the end of the linked list: ";
	cin >> v;
	n->data = v;
	if (head == NULL)
	{
		n->next += NULL;
		head == n;
	}
	else
	{
		current = head;
		while (current->next != NULL)
		{
			current = current->next;
		}
		current->next = n;
		n->next = NULL;
	}
}
void delete_beginning()
{
	struct node* current;
	if (head == NULL)
	{
		cout << "ERROR!" << endl << "The list is empty." << endl;
		return;
	}
	else
	{
		current = head;
		head = head->next;
		delete current;
		return;
	}
}
void delete_end()
{
	struct node* current, * pre_current;
	if (head == NULL)
	{
		cout << "ERROR!" << endl << "The list is empty." << endl;
		return;
	}
	else
	{
		current = head;
		while (current->next != NULL)
		{
			pre_current = current;
			current = current->next;
		}
		pre_current->next = NULL;
		delete current;
		return;
	}
}
void display()
{
	struct node* temp = head;
	if (head == NULL)
	{
		cout << endl << "The Linked List is empty.";
		return;
	}
	else
	{
		cout << endl << "The current linked list is [";
		while (temp != NULL)
		{
			cout << " " << temp->data;
			temp = temp->next;
		}
		cout << " ]" << endl;
		return;
	}
}
int main()
{
	int the_selected_selection;
	cout << "This is a program showcasing the following functions of a linked list." << endl;
	do
	{
		cout << endl << "1. Insert an element at the beginning of the linked list." << endl;
		cout << "2. Insert an element at the end of the linked list." << endl;
		cout << "3. Delete an element from the beginning of the linked list." << endl;
		cout << "4. Delete an element from the end of the linked list." << endl;
		cout << "5. Display the current linked list." << endl;
		cout << "6. Exit." << endl;
		cout << endl << "Select any one of the available functions:";
		cin >> the_selected_selection;
		switch (the_selected_selection)
		{
		case 1:
		{
			insert_beginning();
			break;
		}
		case 2:
		{
			insert_end();
			break;
		}
		case 3:
		{
			delete_beginning();
			break;
		}
		case 4:
		{
			delete_end();
			break;
		}
		case 5:
		{
			display();
			break;
		}
		case 6:
		{
			cout << endl << "Thank you using this program!" << endl << "Program terminated...";
			return 0;
		}
		default:
		{
			cout << "ERROR!" << endl << "Please enter a valid selection" << endl << " " << endl;
			break;
		}
		}
	} while (the_selected_selection != 100);
}