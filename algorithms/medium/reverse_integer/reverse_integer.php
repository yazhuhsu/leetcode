<?php

class Solution {

    /**
     * @param Integer $x
     * @return Integer
     */
    function reverse($x) {
        $result = 0;
        $min = -pow(2, 31);
        $max = pow(2, 31) - 1;
        
        while($x) {
            if($result*10 > $min && $result*10 < $max) {
                $result *= 10;
                $result += (int)$x%10;
                $x = (int)$x/=10;
            } else {
                return 0;
            }
        }
        
        return $result;
    }
}

?>