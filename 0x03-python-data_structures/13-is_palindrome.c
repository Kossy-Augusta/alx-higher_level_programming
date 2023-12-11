#include <stdlib.h>
#include "lists.h"

/**
 * add_node - adds a new node at the beginning of a linked list list_t
 * @head: double pointer to  list_t
 * @n: new integar to be added to list
 *
 * Return: the address of the new element, or NULL if it fails
 */
listint_t *add_node(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;

	return (*head);
}

/**
 * pop_node - transverses the new list to check the value of n
 * @head: double pointer to  list_t
 *
 * Return: the value of the inteager at the begginig of list,
 * -1 if it is an empty list
 */
int check_node_value(listint_t **head)
{
	listint_t *temp = *head;
	int data;

	if (temp == NULL)
		return (-1);
	data = temp->n;
	*head  = temp->next;

	return (data);
}
/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @head: double pointer to beggingig of list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *temp = NULL, *temp2;
	int node_data;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	slow = *head;
	fast = *head;

	while (fast != NULL && fast->next)
	{
		add_node(&temp, slow->n);
		fast = fast->next->next;
		slow = slow->next;
	}
	if (fast != NULL)
		slow = slow->next;
	temp2 = temp;
	while (slow != NULL)
	{
		node_data = check_node_value(&temp);
		if (node_data != slow->n)
			return (0);
		slow = slow->next;
	}
	free_listint(temp2);

	return (1);
}
