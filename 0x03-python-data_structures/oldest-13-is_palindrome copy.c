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
	int rev_array[30] = {0}, iter = 0, old_ind = 29;
	int rev_idx = 29, len = 0, trac = 0, list_len = 0, half = 0;
	listint_t *ptr;

	if (head == NULL || *head == NULL)
		return (1);

	ptr = *head;
	while (ptr != NULL)
	{
		if (iter == 10)
			break;
		rev_array[rev_idx] = ptr->n;
		len++, rev_idx--;
		ptr = ptr->next;
		iter++;
	}
	if (iter == 1)
		return (1);
	ptr = *head, list_len = len;
	half = list_len / 2;

	while (ptr != NULL && trac <= half)
	{
		if (rev_array[old_ind] == ptr->n)
		{
			ptr = ptr->next;
			trac++, rev_idx++, old_ind--;
			continue;
		}
		return (0);
	}
	return (1);
}
