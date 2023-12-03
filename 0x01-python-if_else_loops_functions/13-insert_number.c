#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the first node of the listint_t list
 * @number: integar to be included in the new node
 *
 * Return: address of the new element or nULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp, *prev;
	int i = 0; /* checker variable */

	new = malloc(sizeof(listint_t));/* create new node */
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	temp = *head;
	prev = temp;
	while (temp && (temp->n < new->n))
	{
		prev = temp;
		temp = temp->next;
		i++;
	}
	if (i == 0)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	new->next = temp;
	prev->next = new;

	return (new);
}
