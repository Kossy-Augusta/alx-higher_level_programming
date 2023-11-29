#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if singly linked list has a cycle in it
 * @list: pointer to linked list
 *
 * Return: 0 if no cycle is found, 1 if cycle is detected
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (list == NULL || list->next == NULL)
		return (0);
	slow = list;
	fast = list->next;
	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}

