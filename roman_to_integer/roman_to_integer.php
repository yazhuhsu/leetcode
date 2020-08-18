<?php
class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function romanToInt($s) {
        
        $r = str_split($s);
        $result = 0;
        
        for($i = 0; $i < count($r); $i++){
            switch($r[$i]){
                case 'I':
                    if ($r[$i+1] == 'V' || $r[$i+1] == 'X') {
                        $result -= 1;   
                    } else {
                        $result += 1;
                    }
                    break;
                
                case 'V':
                    $result += 5;
                    break;
                
                case 'X':
                    if($r[$i+1] == 'L' || $r[$i+1] == 'C'){
                        $result -= 10;
                    } else {
                        $result += 10;
                    }
                    break;
                
                case 'L':
                    $result += 50;
                    break;
                    
                case 'C':
                    if($r[$i+1] == 'D' || $r[$i+1] == 'M'){
                        $result -= 100;
                    } else {
                        $result += 100;
                    }
                    break;
                    
                case 'D':
                    $result += 500;
                    break;
                
                case 'M':
                    $result += 1000;
                    break;
            }
        }
        
        if($result > 0 && $result < 4000) return $result;
        
        return 0;
    }
}
?>