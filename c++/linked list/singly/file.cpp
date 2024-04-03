#include <iostream>

struct Node
{
    int data;
    Node *next;

    Node(int _data)
    {
        next = nullptr;
        data = _data;
    }
};

void traverse(Node *head);
Node *insertAtBegin(int data, Node *head);
void insertAtPos(int index, int data, Node *head);
void insertAtEnd(int data, Node *head);
bool remove(int index, Node *head);

int main()
{
    Node *head = new Node(1);
    insertAtPos(1, 2, head);
    insertAtPos(2, 3, head);
    remove(2, head);
    insertAtEnd(11, head);
    Node *newHead = insertAtBegin(99, head);
    traverse(newHead);

    return 0;
}

void traverse(Node *head)

{
    while (head != nullptr)
    {
        std::cout << head->data << "\n";
        head = head->next;
    }
}

Node *insertAtBegin(int data, Node *head)
{
    Node *newHead = new Node(data);
    newHead->next = head;
    return newHead;
}

void insertAtPos(int index, int value, Node *head)
{
    int _index = 0;
    Node *prev = nullptr;
    while (_index <= index)
    {
        if (_index == index)
            if (prev != nullptr)
            {
                Node *temp = head;
                Node *newNode = new Node(value);
                prev->next = newNode;
                newNode->next = temp;
                break;
            }
        prev = head;
        head = head->next;
        _index++;
    }
}

void insertAtEnd(int data, Node *head)
{
    while (true)
    {
        if (head->next == nullptr)
        {
            Node *newTail = new Node(data);
            head->next = newTail;
            break;
        }
        head = head->next;
    }
}

bool remove(int index, Node *head)
{
    int _index = 0;
    Node *prev;
    while (true)
    {
        if (head == nullptr)
        {
            return false;
        }
        else
        {
            if (_index == index)
            {
                prev->next = head->next;
                delete head;
                break;
            }
        }
        prev = head;
        head = head->next;
        _index++;
    }
}
