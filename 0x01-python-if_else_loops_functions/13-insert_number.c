#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: pointer to a pointer to the head of the linked list.
 * @number: he number to be inserted
 * Return: 0 If the function fails or pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head, *num;

	num = malloc(sizeof(listint_t));
	if (num == NULL)
		return (NULL);
	num->n = number;

	if (ptr == NULL || ptr->n >= number)
	{
		num->next = ptr;
		*head = num;
		return (num);
	}

	while (ptr != NULL && ptr->next != NULL && ptr->next->n < number)
		ptr = ptr->next;

	num->next = ptr->next;
	ptr->next = num;

	return (num);
}
