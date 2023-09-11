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
	int rev_idx = 39, len = 0, trac = 0;
	listint_t *ptr;

	if (*head == NULL)
		return (1);

	ptr = *head;
	while (ptr != NULL)
	{
		rev_array[rev_idx] = ptr->n;
		len++, rev_idx--;
		ptr = ptr->next;
	}
	ptr = *head, len = rev_idx;
	rev_idx = 39;

	while (ptr != NULL)
	{
		if (rev_array[rev_idx] == ptr->n)
		{
			ptr = ptr->next;
			rev_idx--, trac--;
			continue;
		}
		return (0);
	}

	return (1);
}
