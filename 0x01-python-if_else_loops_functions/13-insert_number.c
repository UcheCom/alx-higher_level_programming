#include "lists.h"

/**
 * insert_node - This inserts a number into a sorted singly-linked list.
 * @head: Pointer to the head of the linked list.
 * @number: The number to insert.
 *
 * Return: NULL - If the function fails.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *nw;

	nw = malloc(sizeof(listint_t));
	if (nw == NULL)
		return (NULL);
	nw->n = number;

	if (node == NULL || node->n >= number)
	{
		nw->next = node;
		*head = nw;
		return (nw);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	nw->next = node->next;
	node->next = nw;

	return (nw);
}
