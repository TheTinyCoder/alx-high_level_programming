#include "lists.h"
#include "stdio.h"

/**
 * check_cycle - function entry-point
 *
 * Description: prints all the elements of a list_t list
 * @head: pointer to singly linked list
 * Return: 1 if there is a cycle, 0 otherwise
 */

int check_cycle(listint_t *head)
{
	nodePtr temp1, temp2;

	if (head)
	{
		temp1 = temp2 = head;
		while (temp1 && temp2 && temp2->next)
		{
			temp1 = temp1->next;
			temp2 = temp2->next->next;
			if (temp1 == temp2)
				return (1);
		}
	}
	return (0);
}
