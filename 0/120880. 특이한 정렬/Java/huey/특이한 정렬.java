import java.util.*;

class Solution {
    public int[] solution(int[] numlist, int n) {
        int[] answer = Arrays.stream(numlist)
            .boxed()
            .sorted(Comparator.
                <Integer>comparingInt(k -> Math.abs(n - k))
                .thenComparingInt(k -> - k)
            )
            .mapToInt(Integer::intValue)
            .toArray();
        return answer;
    }
}