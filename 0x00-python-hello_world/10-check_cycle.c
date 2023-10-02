#include "lists.h"

/**
 * check_cycle - Checks if a linked list has a cycle
 * by using the tortoise and hare algorithm
 * @list: Pointer to the head of the node
 * Return: 1 if there's a cycle, 0 (Otherwise)
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr = list, *fast_ptr = list;

	while (slow_ptr && fast_ptr && fast_ptr->next)
	{
		slow_ptr = slow_ptr->next; /*Move one step*/
		fast_ptr = fast_ptr->next; /*Move two steps*/

		if (slow_ptr == fast_ptr)
			return  (1);
	}
	return (0);
}

