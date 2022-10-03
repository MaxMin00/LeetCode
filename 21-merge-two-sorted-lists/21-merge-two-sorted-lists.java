/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        //dummy node
        ListNode dummy = new ListNode();
        ListNode temp = dummy;
            
        //compare two values
        while (list1 != null || list2 != null) {
            //current node is null. return other node
            if (list1 == null) {
                temp.next = list2;
                list2 = list2.next;
                break;
            }
            if(list2 == null) {
                temp.next = list1;
                list1 = list1.next;
                break;
            }
            if (list1.val > list2.val) {
                temp.next = list2;
                list2 = list2.next;
                } else {
                temp.next = list1;
                list1 = list1.next;
            }
        temp = temp.next;
        }
        
        return dummy.next;
    }
}