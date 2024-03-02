import java.util.*;
class Solution {
    public static int[] sortedSquares(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            nums[i] = nums[i] * nums[i];
        }
        Arrays.sort(nums);
        return nums;
    }

    public static void main(String args[]) {
        int[] nums = {};
        int[] result = sortedSquares(nums);
        // Print the result or perform further operations
        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}
