#include "lists.h"

/**
 * insert_node - Inserts node
 * @head: Head of the linked list
 * @number: number to be added to the list
 * Return: Pointer to a node or null if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new_node = NULL;
	listint_t *temp = NULL;

	(void)number;

	if (head == NULL || *head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	/* Traverse the list to find where current->n > number*/
	while (current->n < number && current != NULL)
	{
		if (current->next->n > number)
			break;
		current = current->next;
	}
	new_node->n = number;
	temp = current->next;
	current->next = new_node;
	new_node = temp;

	return (NULL);
}
