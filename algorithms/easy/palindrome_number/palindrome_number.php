<?php

class Solution {
    /**
     * @param Integer $x
     * @return Boolean
     */
    function isPalindrome($x) {
        if($x < 0) {
            return false;
        }
        
        $result = 0;
        $original = $x;
        
        while($x){
            $result *= 10;
            $result += (int)$x%10;
            $x = (int)$x/=10;
        }
        
        if($result == $original){
            return true;
        }
        
        return false;
    }
}

?>