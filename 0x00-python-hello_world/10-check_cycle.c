#include "lists.h"

/**
 * check_cycle - looks for cycle in a linked list
 * @list: list stuct pointer
 * Return: 0 if not found and 1 if found
 */

int check_cycle(listint_t *list)
{
	listint_t *list_copy;
	listint_t *last_list;

	list_copy = list;
	last_list = list;
	
	while (list && list_copy && list_copy->next)
	{
		list = list->next;
		list_copy = list_copy->next->next;
		
		if (list == list_copy)
		{
			list = last_list;
			last_list =  list_copy;

			while (1)
			{
				list_copy = last_list;
				
				while (list_copy->next != list && list_copy->next != last_list)
				{
					list_copy = list_copy->next;
				}
				if (list_copy->next == list)
					break;
				list = list->next;
			}
			return (1);
		}
	}
	return (0);
}
