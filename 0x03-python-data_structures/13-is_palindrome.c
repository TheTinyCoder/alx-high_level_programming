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
	nodePtr temp;
	int x = 0, y = 0, *z;

	if (*head)
	{
		for (temp = *head; temp; temp = temp->next)
			x++;
		z = malloc(sizeof(int) * (x + 1));
		if (!z)
			return (0);
		for (temp = *head; temp; temp = temp->next)
			z[y] = temp->n, y++;
		x -= 1;
		for (y = 0; y != x && y < x; y++)
		{
			printf("(y:%d - x:%d)\n", y, x);
			if (z[y] != z[x])
			{
				free(z);
				return (0);
			}
			x--;
		}
		free(z);
	}
	return (1);
}
