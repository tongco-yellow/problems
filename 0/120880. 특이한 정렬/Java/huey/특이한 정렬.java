import java.util.*;

class Solution {
    public int[] solution(int[] numlist, int n) {
        return Arrays.stream(numlist)
            .boxed()
            .sorted(Comparator
                .comparingInt((Integer k) -> Math.abs(n - k))
                .thenComparingInt(k -> - k)
            )
            .mapToInt(Integer::intValue)
            .toArray();
    }
}