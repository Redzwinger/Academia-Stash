#include <iostream>
using namespace std;

long fact(long n)
{
    if(n>1)
    {
        return n * fact(n-1);
    }
    else if(n==1)
    {
        return n;
    }
    return 0;
}

int nacci(int a) 
{
   if(a<=1) 
   {
      return a;
   }
   else
   {
      return nacci(a-1)+nacci(a-2);
   }
}

int main()
{
    int the_selected_selection;
    cout<<"\n\t\tThis program showcases the following functions based on the concept of Recursion."<<endl;
    do
    {
        cout<<endl<<"1. Calculate factorial of an integer."<<endl;
        cout<<"2. Form a Fibonacci series. "<<endl;
        cout<<"3. Exit."<<endl;
        cout<<endl<<"Please select any one of the available functions: ";
        cin>>the_selected_selection;
        
        switch (the_selected_selection)
        {
            case 1:
            {
                long facto_int;
                cout<<"\nPlease enter the integer for which factorial is to be calculated: ";
                cin>>facto_int;
                cout<<"\nThe factorial of "<< facto_int <<" is "<<fact(facto_int)<<"."<<endl;
                break;
            }
            case 2:
            {
                int fibo, behold_the_power_of_recursion=0;
                cout<<"\nPlease enter the number of terms in the Fibonacci series that is to be generated: ";
                cin>>fibo;
                cout<<"\nThe Fibonacci series containing "<< fibo <<" terms is [";
                
                while(behold_the_power_of_recursion < fibo) 
                {
                    cout << " " << nacci(behold_the_power_of_recursion);
                    behold_the_power_of_recursion++;
                }
                
                cout<<" ]."<<endl;
                break;
            }
            case 3:
            {
                cout<<endl<<"Thank you using this program!"<<endl<<"Program terminated...";
                return 0;
            }
            default:
            {
                cout<<"ERROR!"<<endl<<"Please enter a valid selection"<<endl<<" "<<endl;
                break;
            }
        }
    }
    while(the_selected_selection!=10);
}
