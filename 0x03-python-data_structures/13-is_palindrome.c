#include "lists.h"

/**
 * list_rev - reverses list
 * @head: pointer to 1st node
 * Return: pointer to node in new list
 */
void list_rev(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = *head;
	listint_t *current = NULL;

	while (next)
	{
		current = next->next;
		next->next = prev;
		prev = next;
		next = current;
	}
	*head = prev;
}

/**
 * is_palindrome - checks if palindrome
 * @head: pointer to a linked list
 * Return: 1 on success, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slw = *head, *fast = *head, *c = *head, *sec_half = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			sec_half = slw->next;
			break;
		}
		if (!fast->next)
		{
			sec_half = slw->next->next;
			break;
		}
		slw = slw->next;
	}
	list_rev(&sec_half);

	while (sec_half && c)
	{
		if (c->n == sec_half->n)
		{
			sec_half = sec_half->next;
			c = c->next;
		}
		else
		{
			return (0);
		}
	}
	if (!sec_half)
		return (1);
	return (0);
}
