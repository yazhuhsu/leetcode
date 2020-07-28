<?php
class Solution {

    /**
     * @param String[] $strs
     * @return String
     */
    function longestCommonPrefix($strs) {
        
        if(count($strs) == 0) return "";
        if(count($strs) == 1) return $strs[0];
        
        $min = PHP_INT_MAX;
        $min_pos = 0;
        
        for($j = 0; $j < count($strs); $j++){
            if(strlen($strs[$j]) < $min){
                $min = strlen($strs[$j]);
                $min_pos = $j;
            }
        }
        
        $min_strs = str_split($strs[$min_pos]);
        
        $same = true;
        $pos = 0;
        for($k = 0; $k < $min; $k++) {
            for($l = 0; $l < count($strs); $l++){
                $m = str_split($strs[$l]);
                if($m[$k] != $min_strs[$k]) $same = false;
            }
            if(!$same) break;
            $pos++;
        }
        
        $result = "";
        for($n = 0; $n < $pos; $n++){
            $result .= $min_strs[$n];
        }
        
        return $result;
    }
}
?>