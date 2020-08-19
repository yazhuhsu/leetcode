<?php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function removeDuplicates(&$nums) {
        $j = $nums[0];
        $num = count($nums);
        for($i = 1; $i < $num; $i++){
            if($nums[$i] == $j){
                unset($nums[$i]);
            } 
            if($j < $nums[$i]){
                $j = $nums[$i];
            }
        }
        
        return count($nums);
    }
}
?>