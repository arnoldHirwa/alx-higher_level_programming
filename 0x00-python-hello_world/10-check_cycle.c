#include "lists.h"

/**
* check_cycle - find a cycle in a loop
* @list: a list to loop through
*
* Return: 1 if loop is found, 0 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *current;

	while (list != NULL)
	{
		current = list->next;
		while (current != NULL)
		{
			if (current == list)
				return (1);
			current = current->next;
		}
		list = list->next;
	}
	return (0);
}
