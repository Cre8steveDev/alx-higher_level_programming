#include <stddef.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a linkedList is a palindrome
 * @head: Double pointer to the head of a list
 * Return: 0 if not else 1
 */

int is_palindrome(listint_t **head)
{
	int rev_array[40] = {0};
	int rev_idx = 39, len = 0, trac = 0, list_len = 0;
	listint_t *ptr;

	if (head == NULL || *head == NULL)
		return (1);

	ptr = *head;
	while (ptr != NULL)
	{
		rev_array[rev_idx] = ptr->n;
		len++, rev_idx--;
		ptr = ptr->next;
	}
	ptr = *head, list_len = len;
	rev_idx++;

	while (ptr != NULL && trac <= (list_len / 2) - 1)
	{
		if (rev_array[rev_idx] == ptr->n)
		{
			ptr = ptr->next;
			trac++, rev_idx++;
			continue;
		}
		return (0);
	}
	return (1);
}
