#include "lists.h"

/**
 * list_rev - reverses list
 * @head: pointer to 1st node
 * Return: pointer to node in new list
 */
void list_rev(listint_t **head)
{
	listint_t *first = NULL;
	listint_t *second = *head;
	listint_t *third = NULL;

	while (second)
	{
		third = second->next;
		second->next = first;
		first = second;
		second = third;
	}
	*head = first;
}

/**
 * is_palindrome - checks if palindrome
 * @head: pointer to a linked list
 * Return: 1 on success, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *a = *head, *b = *head, *c = *head, *d = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		b = b->next->next;
		if (!b)
		{
			d = a->next;
			break;
		}
		if (!b->next)
		{
			d = a->next->next;
			break;
		}
		a = a->next;
	}
	list_rev(&d);

	while (d && c)
	{
		if (c->n == d->n)
		{
			d = d->next;
			c = c->next;
		}
		else
		{
			return (0);
		}
	}
	if (!d)
		return (1);
	return (0);
}
