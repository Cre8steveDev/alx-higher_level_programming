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
	listint_t *ptr;
	int array[3000] = {0};
	int len = 0, r_idx = 2999;

	if (head == NULL)
		return (1);

	ptr = *head;

	if (ptr == NULL || ptr->next == NULL)
		return (1);

	while (ptr != NULL)
	{
		array[r_idx] = ptr->n;
		len++;
		r_idx--;
		ptr = ptr->next;
	}
	ptr = *head;
	r_idx++;

	while (ptr != NULL)
	{
		if (ptr->n != array[r_idx])
			return (0);
		r_idx++;
		ptr = ptr->next;
	}

	return (1);
}
