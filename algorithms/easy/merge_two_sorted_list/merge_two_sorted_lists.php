<?php

/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */
class Solution {

    /**
     * @param ListNode $l1
     * @param ListNode $l2
     * @return ListNode
     */
    function mergeTwoLists($l1, $l2) {
        
        if($l1 == null && $l2 == null) return null;
        if($l1 == null && $l2 != null) return $l2;
        if($l1 != null && $l2 == null) return $l1;
        
        if($l1->val <= $l2->val){
            $l3 = $l1;
            $l1 = $l1->next;
        } else {
            $l3 = $l2;
            $l2 = $l2->next;
        }
        
        $result = $l3;

        while($l1 !== null && $l2 !== null){
            if($l1->val <= $l2->val){
                $l3->next = $l1;
                $l1 = $l1->next;
            } else {
                $l3->next = $l2;
                $l2 = $l2->next;
            }
            $l3 = $l3->next;
        }
        
        while(!is_null($l1)){
            $l3->next = $l1;
            $l1 = $l1->next;
            $l3 = $l3->next;
        }
        
        while(!is_null($l2)){
            $l3->next = $l2;
            $l2 = $l2->next;
            $l3 = $l3->next;
        }
        
        return $result;
    }
}

?>