import java.util.*;
import java.util.stream.IntStream;

class Solution {
    public int solution(int[][] lines) {
        int answer = 0;
        Map<Integer, Integer> bigLine = new HashMap<>();
        for(int[] smallLine: lines) {
            for (int i = smallLine[0]; i < smallLine[1]; i++) {
                bigLine.putIfAbsent(i, 0);
                bigLine.put(i, bigLine.get(i) + 1);
                if (bigLine.get(i) == 2) answer++;
            }
        }
        return answer;
    }
}