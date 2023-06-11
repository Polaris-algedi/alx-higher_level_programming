/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int i, j, size = 0, *list;
	listint_t *current = *head;
	/* Count the size of the linked list */
	while (current)
	{
		size++;
		current = current->next;
	}

	if (size % 2 != 0)
		return (0);
	if (size == 0)
		return (1);
	/* Create the list */
	list = malloc(sizeof(int) * size);
	if (list == NULL)
	{
		return (0);
	}
	/* fill up the list */
	current = *head;
	for (i = 0; current; i++)
	{
		list[i] = current->n;
		current = current->next;
	}
	/* Check if the list is palindrome */
	for (i = 0, j = size - 1; i < size / 2; i++, j--)
	{
		if (list[i] != list[j])
			return (0);
	}
	return (1);
}
