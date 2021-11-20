<?php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function isValid($s) {
        $len = strlen($s);
        if($len == 0) return true;
        if($len % 2 == 1) return false;
        
        if($s[0] == ')' || $s[0] == ']' || $s[0] == '}') return false;
        if($s[$len-1] == '(' || $s[$len-1] == '[' || $s[$len-1] == '{') return false;
        
        $ss = [];
        $ss_len = 0;
        
        for($i = 0; $i < strlen($s); $i++){
            if($s[$i] == '(' || $s[$i] == '[' || $s[$i] == '{'){
                $ss[$ss_len] = $s[$i];
                $ss_len++;
            } elseif($s[$i] == ')'){
                if($ss[$ss_len-1] != '(') return false;
                elseif($ss[$ss_len-1] == '('){
                    array_pop($ss);
                    $ss_len--;
                }
            } elseif($s[$i] == ']'){
                if($ss[$ss_len-1] != '[') return false;
                elseif($ss[$ss_len-1] == '['){
                    array_pop($ss);
                    $ss_len--;
                }
            } elseif($s[$i] == '}'){
                if($ss[$ss_len-1] != '{') return false;
                elseif($ss[$ss_len-1] == '{'){
                    array_pop($ss);
                    $ss_len--;
                }
            }
        }
        
        return true;
    }
}
?>