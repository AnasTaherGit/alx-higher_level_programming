#include "lists.h"

/**
 * is_palindrome - Validates if a linked list is a palindrome
 * @head: Double pointer to the head of the linked list
 *
 * Return: 1 if it is a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slowPtr = *head, *fastPtr = *head, *tempPtr = *head;
	listint_t *duplicatedList = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		fastPtr = fastPtr->next->next;
		if (!fastPtr)
		{
			duplicatedList = slowPtr->next;
			break;
		}
		if (!fastPtr->next)
		{
			duplicatedList = slowPtr->next->next;
			break;
		}
		slowPtr = slowPtr->next;
	}
	flipLinkedList(&duplicatedList);
	while (duplicatedList && tempPtr)
	{
		if (tempPtr->n == duplicatedList->n)
		{
			duplicatedList = duplicatedList->next;
			tempPtr = tempPtr->next;
		}
		else
			return (0);
	}
	if (!duplicatedList)
		return (1);
	return (0);
}

/**
 * flipLinkedList - Flips the linked list
 * @head: pointer to the head node of the list
 *
 * Return: pointer to the head node of the flipped list
 */
void flipLinkedList(listint_t **head)
{
	listint_t *previousNode = NULL;
	listint_t *currentNode = *head;
	listint_t *nextNode = NULL;

	while (currentNode)
	{
		nextNode = currentNode->next;
		currentNode->next = previousNode;
		previousNode = currentNode;
		currentNode = nextNode;
	}

	*head = previousNode;
}
