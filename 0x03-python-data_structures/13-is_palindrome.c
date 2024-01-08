#include "lists.h"

/**
 * is_palindrome_recursive - check if list is a palindrome using recursion
 * @left: left pointer
 * @right: right pointer
 *
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome_recursive(listint_t **left, listint_t *right)
{
	int response;

	if (right != NULL)
	{
		response = is_palindrome_recursive(left, right->next);
		if (response != 0)
		{
			response = ((*left)->n == right->n);
			*left = (*left)->next;
			return (response);
		}
		return (0);
	}
	return (1);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of linked list
 *
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);

	return (is_palindrome_recursive(head, *head));
}

