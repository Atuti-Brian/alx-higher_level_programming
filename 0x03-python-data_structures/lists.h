#include <stddef.h>
#ifndef CUSTOM_LISTS_H
#define CUSTOM_LISTS_H

/**
 * struct CustomListNode - singly linked list
 * @value: integer value stored in the node
 * @next: points to the next node
 *
 * Description: structure for a singly linked list node
 */
typedef struct CustomListNode
{
    int value;
    struct CustomListNode *next;
} CustomListNode;

size_t custom_print_list(const CustomListNode *head);
CustomListNode *custom_add_node_end(CustomListNode **head, const int value);
void custom_free_list(CustomListNode *head);

int custom_is_palindrome(CustomListNode **head);

#endif /* CUSTOM_LISTS_H */

