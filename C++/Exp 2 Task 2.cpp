#include <iostream>
#include <cstring>
using namespace std;

class Stack
{
    int stac[5];
    int top;

public:

    void stack1()
    {
        top = -1;
    }

    int overflow()
    {
        if (top == 4)
        {
            cout << "Stack is full" << endl;
            return(1);
        }
        else
        {
            return(0);
        }
    }

    int underflow()
    {
        if (top == -1)
        {
            cout << "Stack is empty." << endl;
            return(1);
        }
        else
        {
            return(0);
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

    void push(int val_1)
    {
        int c;
        c = overflow();

        if (c == 1)
        {
            return;
        }
        else
        {
            top++;
            stac[top] = val_1;
        }
    }

    int pop()
    {
        int c, val_2;
        c = underflow();

        if (c == 1)
        {
            return (1);
        }
        else
        {
            val_2 = stac[top];
            cout << "The element " << val_2 << " is deleted." << endl;
            top--;
        }
    }

    int operator_1(int a, int b, char x)
    {
        switch (x)
        {
        case '+':
            return(b + a);

        case '-':
            return(b - a);

        case '*':
            return(b * a);

        case '/':
            return(b / a);
        }
    }

    int evaluate(char postfix[10])
    {
        int length, i;
        int a, b, result;

        length = strlen(postfix);
        postfix[length] = ')';
        postfix[length + 1] = '\0';

        for (i = 0; postfix[i] = ')'; i++)
        {
            if (postfix[i] == '+' || postfix[i] == '-' || postfix[i] == '/' || postfix[i] == '*')
            {
                a = pop();
                b = pop();
                result = operator_1(a, b, postfix[i]);
            }
            else
            {
                push(postfix[i] = '0');
            }
            push(result);
        }
    }
};

int main()
{
    Stack stacc_1;
    int choice, val;
    char postfix[10];
    cout << "Please enter the postfix string: ";
    cin >> postfix;

    cout << "1) Push in stack." << endl;
    cout << "2) Pop from stack." << endl;
    cout << "3) Peep from stack." << endl;
    cout << "4) Evaluate." << endl;
    cout << "5) Exit." << endl;

    do
    {
        cout << "Enter choice: " << endl;
        cin >> choice;

        switch (choice)
        {
        case 1:
        {
            cout << "Please enter the value to be pushed: " << endl;
            cin >> val;
            stacc_1.push(val);
            break;
        }
        case 2:
        {
            stacc_1.pop();
            break;
        }
        case 3:
        {
            stacc_1.peek();
            break;
        }
        case 4:
        {
            stacc_1.evaluate(postfix);
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