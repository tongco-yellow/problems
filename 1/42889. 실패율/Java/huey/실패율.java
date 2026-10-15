import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        int[][] result = new int[N][3];
        for (int i = 0; i < N; i++) {
            result[i][0] = i + 1;
            for (int j: stages) {
                if (j >= i + 1) {
                    result[i][1] += 1;
                }
                if (j == i + 1) {
                    result[i][2] += 1;
                }
            }
        }
        
        return Arrays.stream(result)
            .sorted(Comparator.comparingDouble(
                r -> (double) r[1] / r[2]
            ))
            .mapToInt(r -> r[0])
            .toArray();
    }
}