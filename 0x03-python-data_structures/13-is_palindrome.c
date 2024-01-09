#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverse a linked list
 * @head: Pointer to the head of the list
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL, *current = head, *next;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}

/**
 * is_palindrome - Check if a linked list is a palindrome
 * @head: Pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return 1;  // Empty list or single-node list is a palindrome

    listint_t *slow = *head, *fast = *head, *second_half;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        slow = slow->next;
    }

    // If the length of the list is odd, move slow one step forward
    if (fast != NULL)
        slow = slow->next;

    second_half = reverse_list(slow);
    slow = *head;

    while (second_half != NULL)
    {
        if (slow->n != second_half->n)
        {
            reverse_list(&second_half);  // Restore the second half
            return 0;  // Not a palindrome
        }

        slow = slow->next;
        second_half = second_half->next;
    }

    reverse_list(&second_half);  // Restore the second half
    return 1;  // It is a palindrome
}

