#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * rev_list - Reverses a linked list
 * @head: Pointer to the head of the list
 * Return: Pointer to the new head of the reversed list
 */
listint_t *rev_list(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - Check if a linked list is a palindrome
 * @head: Pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slw, *quick, *sec_half;
	slw = *head;
	quick = *head;

	while (quick != NULL && quick->next != NULL)
	{
		quick = quick->next->next;
		slw = slw->next;
	}

	if (quick != NULL)
		slw = slw->next;

	sec_half = rev_list(slw);
	slw = *head;

	while (!sec_half)
	{
		if (slw->n != sec_half->n)
		{
			rev_list(sec_half);
			return (0);
		}

		slw = slw->next;
		sec_half = sec_half->next;
	}

	rev_list(sec_half);
	return (1);
}
