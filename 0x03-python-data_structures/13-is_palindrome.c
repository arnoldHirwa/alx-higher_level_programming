#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * checkPal - check if a list is palindrome
 * @array: pointer to list
 * @index_a: primero indice (inicial)
 * @index_b: seg indice (final)
 * Return: return 1 if list is palindrome or 0 otherwise
 */
int checkPal(int *array, int index_a, int index_b)
{
	if (index_a > index_b)
		return (1);
	if (array[index_a] != array[index_b])
	{
		return (0);
	}
	return (checkPal(array, index_a + 1, index_b - 1));
}
/**
 * is_palindrome - check if a single linked list is palindrome
 * @head: pointer to node listint_t
 * Return: return 1 if list is palindrome or 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int len = 0;
	int i = 0; /*, j = 0, node_a = 0, node_b = 0, index_a = 0, index_b = 0;*/
	const listint_t *temp = *head;
	int *array;

	if (!*head)
		return (1);
	while (temp)
	{
		temp = temp->next;
		len++;
	}
	temp = *head;
	array = malloc(sizeof(int) * len);
	if (!array)
		return (0);
	for (i = 0; i <= (len - 1); i++)
	{
		array[i] = temp->n;
		temp = temp->next;
	}
	if (checkPal(array, 0, len - 1) == 1)
	{
		free(array);
		return (1);
	}
	free(array);
	return (0);
}
