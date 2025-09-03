#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int numberOfPairs(vector<vector<int>>& points) {
        int ans = 0;
        int n = points.size();

        // Sort points by x ascending, and if tie, by y descending
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
            if (a[0] == b[0]) return a[1] > b[1];
            return a[0] < b[0];
        });

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {  
                // we know points[i].x <= points[j].x due to sorting
                if (points[i][1] < points[j][1]) continue;

                bool illegal = false;
                for (int k = i + 1; k < j; k++) {  
                    if (points[k][1] <= points[i][1] && points[k][1] >= points[j][1]) {
                        illegal = true;
                        break;
                    }
                }
                if (!illegal) ans++;
            }
        }
        return ans;
    }
};
