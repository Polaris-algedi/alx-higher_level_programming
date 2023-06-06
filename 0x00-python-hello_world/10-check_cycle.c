#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: linked list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;
	listint_t *faster = list;

	if (!list)
		return (0);

	while (slow && fast && faster && fast->next && faster->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		faster = faster->next->next->next;

		if (slow == fast || slow == faster)
			return (1);
	}
	return (0);
}
