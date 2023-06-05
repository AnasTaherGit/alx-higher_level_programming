#include "lists.h"
#include <stdbool.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *BasePointer = list;
	listint_t *RunnerPointer = list;
	bool exit = true;

	if (list == NULL)
		return (0);

	if (BasePointer == NULL || RunnerPointer == NULL)
		exit = false;
	else if (RunnerPointer->next == NULL)
		exit = false;

	while (exit)
	{
		BasePointer = BasePointer->next;
		RunnerPointer = RunnerPointer->next->next;
		if (BasePointer == RunnerPointer)
			return (1);
		if (BasePointer == NULL || RunnerPointer == NULL)
			exit = false;
		else if (RunnerPointer->next == NULL)
			exit = false;
	}
	return (0);
}
