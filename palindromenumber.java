class Solution {
    public boolean isPalindrome(int x) {
        String xString = String.valueOf(x);
        int n = xString.length();

        for (int i = 0; i < n/2; i++) {
          if (xString.charAt(i) != xString.charAt(n - i - 1)) {
          return false;
          }

        }
        return true;
    }
}