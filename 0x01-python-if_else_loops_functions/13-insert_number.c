#include "lists.h"
#include "stdio.h"

/**
 * insert_node - function entry-point
 *
 * Description: inserts a number into a sorted singly linked list
 * @head: pointer to singly linked list
 * @number: number to insert
 * Return: address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	nodePtr new, temp;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (*head && (*head)->n < number)
	{
		temp = *head;
		while (temp)
		{
			if (!temp->next)
			{
				temp->next = new;
				break;
			}
			else if (temp->next->n > number)
			{
				new->next = temp->next;
				temp->next = new;
				break;
			}
			temp = temp->next;
		}
	}
	else
	{
		new->next = *head;
		*head = new;
	}
	return (*head);
}
