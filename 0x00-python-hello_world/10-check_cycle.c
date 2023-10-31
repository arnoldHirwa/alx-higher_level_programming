#include "lists.h"

/**
* check_cycle - find a cycle in a loop
* @list: a list to loop through
*
* Return: 1 if loop is found, 0 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *first, *last;

	if (list == NULL || list->next == NULL)
		return (0);

	first = list->next;
	last = list->next->next;

	while (first && last && last->next)
	{
		if (first == last)
			return (1);

		first = first->next;
		last = last->next->next;
	}

	return (0);
}
