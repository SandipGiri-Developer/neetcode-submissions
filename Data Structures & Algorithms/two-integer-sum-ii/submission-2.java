class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int n = numbers.length;
        for(int i = 1;i<n;i++){
            for(int j = i;j<n;j++){
                if(numbers[j] + numbers[j-i] == target){
                    return new int[]{j-i, j};
                }
            }
        }
        return new int[0];
    }
}
