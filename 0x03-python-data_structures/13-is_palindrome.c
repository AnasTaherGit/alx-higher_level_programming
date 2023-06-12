#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

/**
 * reverse - reverses a linked list
 * @head: pointer to the head of the list
 * Return: pointer to the head of the reversed list
 */
listint_t *reverse(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next;

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
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the singly linked list
 * Return: 1 if palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *second_half, *prev_slow = *head;
	listint_t *midnode = NULL;
	int res = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}
		if (fast != NULL)
		{
			midnode = slow;
			slow = slow->next;
		}
		second_half = slow;
		prev_slow->next = NULL;
		reverse(second_half);
		res = compareLists(*head, second_half);

		reverse(second_half);
		if (midnode != NULL)
		{
			prev_slow->next = midnode;
			midnode->next = second_half;
		}
		else
			prev_slow->next = second_half;
	}
	return (res);
}

/**
 * compareLists - compares two linked lists
 * @head1: double pointer to the head of the singly linked list
 * @head2: double pointer to the head of the singly linked list
 * Return: 1 if palindrome, otherwise 0
 */
int compareLists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 && temp2)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
			return (0);
	}
	if (temp1 == NULL && temp2 == NULL)
		return (1);
	return (0);
}
