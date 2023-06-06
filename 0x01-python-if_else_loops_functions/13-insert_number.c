#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to the listint_t list
 * @number: integer
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	unsigned int i;
	listint_t *new, *temp;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;
	if ((*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	temp = *head;
	while (temp)
	{
		if (temp->next)
		{
			if (temp->n <= number && temp->next->n >= number)
			{
				new->next = temp->next;
				temp->next = new;
				return (new);
			}
		}
		else
		{
			temp->next = new;
			return (new);
		}
		temp = temp->next;
	}
	free(new);
	return (NULL);
}
