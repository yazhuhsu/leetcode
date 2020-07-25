<?php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        $result = [];
        for ($i = 0; $i < count($nums)-1; $i++) {
            for ($j = $i+1; $j < count($nums); $j++) {
                if ($nums[$i] + $nums[$j] == $target) {
                    $result[] = $i;
                    $result[] = $j;
                    break;
                }
            }
            
            if(count($result) == 2) break;
        }
        
        return $result;
    }
}

$file = fopen("two_sum.txt", "r+");
$file_content = fread($file, filesize("two_sum.txt"));
fclose($file);

$input = explode("\n", $file_content);

$solution = new Solution();
for($i = 0; $i < count($input); $i+=2){
    $input_num = str_replace("[", "", $input[$i]);
    $input_num = str_replace("]", "", $input_num);
    $nums = explode(", ", $input_num);
    $target = (int)$input[$i+1];
    print_r($solution->twoSum($nums, $target));
}

?>