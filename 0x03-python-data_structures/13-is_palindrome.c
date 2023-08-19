/*
 * File: 13-is_palindrome.c
 * Author: Uchenna Oko
 */

#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head;
	listint_t *next;
	listint_t *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: 0 - If the linked list is not a palindrome.
 *         1 - If the linked list is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	listint_t *revs;
	listint_t *mid;
	size_t len = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		len++;
		temp = temp->next;
	}

	temp = *head;
	for (i = 0; i < (len / 2) - 1; i++)
		temp = temp->next;

	if ((len % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	revs = reverse_listint(&temp);
	mid = revs;

	temp = *head;
	while (revs)
	{
		if (temp->n != revs->n)
			return (0);
		temp = temp->next;
		revs = revs->next;
	}
	reverse_listint(&mid);

	return (1);
}
