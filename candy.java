class Solution {
    public int candy(int[] ratings) {
        int counter = ratings.length;
        int[] candycount = new int[ratings.length];

        for (int i = 0; i < ratings.length-1; i++) {
            int right = ratings[i+1];
            int cur = ratings[i];


            if (cur > right && (candycount[i] <= candycount[i+1])) {
                counter++;
                candycount[i]++;
                int j = i;
                while (j-1 >= 0 && candycount[j] >= candycount[j-1] && ratings[j-1] > ratings[j]) {
                    candycount[j-1]++;
                    counter++;
                    j--;
                }
            }
                while (right > cur && candycount[i+1] <= candycount[i]) {
                    counter++;
                    candycount[i+1]++;
                }


        }
        return counter;
    }
}
