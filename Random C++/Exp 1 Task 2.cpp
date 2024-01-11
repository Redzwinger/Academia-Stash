#include <iostream>
using namespace std;

void insert(int arr[], int size)
{
    int new_element, pos;
    cout << "Enter the element to be inserted" << endl;
    cin >> new_element;

    cout << "Enter the position of insertion" << endl;
    cin >> pos;
    
    if (pos < size)
    {
        for (int i = size - 1; i >= pos; i--)
        {
            arr[i + 1] = arr[i];
        }

        arr[pos] = new_element;
        size += 1;

        cout << "The array after change is: " << endl;

        for (int i = 0; i < size; i++)
        {
            cout << arr[i] << " ";
        }
    }
}

void del(int arr[], int n)
{
    int i;
    n--;

    for (i = 0; i < n; i++)
    {
        arr[i] = arr[i + 1];
    }
    cout << "The array after change is: " << endl;
    
    for (i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
}

int main()
{
    int element;
    int Array[100];
    int i, sum = 0;

    cout << "Please enter the total number of elements: ";
    cin >> element;

    for (i = 0; i < element; i++)
    {
        cout << "Please enter the #" << i + 1 << " element: ";
        cin >> Array[i];
    }

    cout << "The array according to the given elements is: " << endl;

    for (i = 0; i <= element-1; i++)
    {
        cout << Array[i] << " ";
    }
       
    int choice;
    cout << endl << "Do you wish to insert an element into the array? [1] or Do you wish to delete an element from the array? [2]" << endl;
    cin >> choice;
    if (choice == 1)
    {
        insert(Array, element);
    }
    else if (choice == 2)
    {
        del(Array, element);
    }
           
    for (i = 1; i < element; ++i)
    {
        if (Array[0] < Array[i])
        {
            Array[0] = Array[i];
        }            
    }

    cout << endl << "The largest/highest element = " << Array[0] << endl;

    for (i = 1; i < element; ++i)
    {
        if (Array[0] > Array[i])
        {
            Array[0] = Array[i];
        }            
    }

    cout << "The smallest/lowest element = " << Array[0] << endl;

    for (i = 0; i < element; i++)
    {
        sum = sum + Array[i];
    }

    int average;
    average = sum / element;
    cout << "Sum = " << sum << endl;
    cout << "Average = " << average << endl;
   
    return 0;
}