class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> multiset = new HashMap<>();
        for(int i = 0; i < s.length(); i++){

            multiset.put(s.charAt(i), multiset.getOrDefault(s.charAt(i), 0) + 1);
        }

        for(int i = 0; i < s.length(); i++) {
            if(multiset.get(s.charAt(i)) == 1){
                return i;
            }
        }
        return -1;
    }
}