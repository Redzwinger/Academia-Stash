#include <iostream>

using namespace std;

struct doublenode
{
    struct doublenode *prev;
    struct doublenode *next;
    int data;
};

struct doublenode *head=NULL;
struct doublenode *tail=NULL;

void insert_beginning()
{
    struct doublenode *nd=new doublenode;
    int entered_value;
    
    cout<<"Please enter the coach ID of the coach that is to be inserted at the begining of the train: ";
    cin>>entered_value;
    
    nd->next=NULL;
    nd->data=entered_value;
    nd->prev=NULL;
    
    if(head==NULL)
    {
        head=nd;
        tail=nd;
    }
    else
    {
        head->prev=nd;
        nd->next=head;
        head=nd;
    }
}

void insert_end()
{
    struct doublenode *nd=new doublenode;
    int entered_value;
    
    cout<<"Please enter the coach ID of the coach that is to be inserted at the end of the train: ";
    cin>>entered_value;
    
    nd->next=NULL;
    nd->data=entered_value;
    nd->prev=NULL;
    
    if(tail==NULL)
    {
        head=nd;
        tail=nd;
    }
    else
    {
        tail->next=nd;
        nd->prev=tail;
        tail=nd;
    }
}

void delete_beginning()
{
    struct doublenode *temp;
    temp=head;
    
    if(head==NULL)
    {
        cout<<"There are, currently, no coaches on the train. Please use one of the Insert functions first. \n";
    }
     else if(temp->next==NULL)
    {
        head=NULL;
        tail=NULL;
        cout<<"The coach with coach ID "<<temp->data<<" from the beginning of the train has been removed. \n";
        delete (temp);
    }
    else
    {
        head=head->next;
        head->prev=NULL;
        cout<<"The coach with coach ID "<<temp->data<<" from the beginning of the train has been removed. \n";
    }
    
    delete temp;
}

void delete_end()
{
    struct doublenode *temp;
    temp=tail;
    
    if(tail==NULL)
    {
        cout<<"There are, currently, no coaches on the train. Please use one of the Insert functions first. \n";
    }
    else if(temp->prev==NULL)
    {
        head=NULL;
        tail=NULL;
        cout<<"The coach with coach ID "<<temp->data<<" from the end of the train has been removed. \n";
        delete (temp);
    }
    else
    {
        tail=tail->prev;
        tail->next=NULL;
        cout<<"The coach with coach ID "<<temp->data<<" from the end of the train has been removed. \n";
    }
    
    delete temp;
}

void display_forward()
{
    struct doublenode *temp=head;
    
    if(head==NULL)
    {
        cout<<endl<<"There are, currently, no coaches on the train. Please use one of the Insert functions first.";
        return;
    }
    else
    {
        cout<<endl<<"The current layout of the train, using coach ID's, in the forward direction is [";
        
        while(temp!=NULL)
        {
            cout<<" "<<temp->data;
            temp=temp->next;
        }
        
        cout<<" ]"<<endl;
    }
}

void display_backward()
{
    struct doublenode *temp=tail;
    
    if(head==NULL)
    {
        cout<<endl<<"There are, currently, no coaches on the train. Please use one of the Insert functions first. \n";
        return;
    }
    else
    {
        cout<<endl<<"The current layout of the train, using coach ID's, in the backward direction is [";
        
        while(temp!=NULL)
        {
            cout<<" "<<temp->data;
            temp=temp->prev;
        }
        
        cout<<" ]"<<endl;
    }
}

int main()
{
    
        int the_selected_selection;
        cout<<"\n \t This program inserts and deletes coaches in a given train using the concept of Doubly Linked List.";
        cout<<"\n \t \t Given below is the list of functions that you can perform on the train.";
        cout<<"\n \t      (Note: By default, the train has no coaches in the beginning of the program.)"<<endl;
    do
    {
        cout<<endl<<"1. Insert a coach at the beginning of the train."<<endl;
        cout<<"2. Insert a coach at the end of the train."<<endl;
        cout<<"3. Delete a coach from the beginning of the train."<<endl;
        cout<<"4. Delete a coach from the end of the train."<<endl;
        cout<<"5. Display the current layout of the train in the forward direction."<<endl;
        cout<<"6. Display the current layout of the train in the backward direction."<<endl;
        cout<<"7. Exit."<<endl;
        cout<<endl<<"Please select any one of the available functions: ";
        cin>>the_selected_selection;
        
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
                display_forward();
                break;
            }
            case 6:
            {
                display_backward();
                break;
            }
            case 7:
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
    while(the_selected_selection!=7);
}