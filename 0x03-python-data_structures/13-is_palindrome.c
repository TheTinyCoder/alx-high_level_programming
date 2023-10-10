#include "lists.h"
#include "stdio.h"

/**
 * is_palindrome - function entry-point
 *
 * Description: checks if a singly linked list is a palindrome
 * @head: pointer to singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	nodePtr temp, temp1;
	int x = 0, y = 0;

	if (*head)
	{
		for (temp = *head; temp; temp = temp->next)
			x++;
		temp = *head;
		if (x % 2 == 0)
		{
			for (y = 1; y < x / 2; y++)
				temp = temp->next;
		}
		else
		{
			for (y = 0; y < x / 2; y++)
				temp = temp->next;
		}
		/* reverse other half of list */
		temp1 = reverse_list(&(temp->next));
		temp = *head;
		/* compare first half to second half */
		for (y = 0; y < x / 2; y++)
		{
			if (temp->n != temp1->n)
				return (0);
			temp = temp->next, temp1 = temp1->next;
		}
	}
	return (1);
}


/**
 * reverse_list - reverses a singly linked list
 *
 * @head: pointer to singly linked list
 * Return: pointer to new head of list
 */

listint_t *reverse_list(listint_t **head)
{
	nodePtr temp1, temp2;

	if (*head)
	{
		temp1 = *head;
		while (temp1->next)
		{
			temp2 = *head;
			*head = temp1->next;
			temp1->next = (*head)->next;
			(*head)->next = temp2;
		}
	}
	return (*head);
}
