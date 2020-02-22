/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        auto sol = new ListNode(0);
        ListNode *r = sol;
        int carry = 0;
        while(true) {
            sol->val = (carry + l1->val + l2->val) % 10;
            carry = (carry + l1->val + l2->val) / 10;
            if (l1->next == nullptr && l2->next == nullptr) {
                if (carry == 1) {
                    sol->next = new ListNode(1);
                }
                break;
            }
            sol->next = new ListNode(0);
            sol = sol->next;
            if (l1->next == nullptr) l1->val = 0;
            else l1 = l1->next;
            if (l2->next == nullptr) l2->val = 0;
            else l2 = l2->next;
        }
        return r;
    }
};