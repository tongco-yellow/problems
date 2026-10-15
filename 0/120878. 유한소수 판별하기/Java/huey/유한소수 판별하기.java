class Solution {
    public int solution(int a, int b) {
        int gcd = getGcd(Math.max(a, b), Math.min(a, b));
        b /= gcd;
        while (true) {
            if (b % 2 != 0) break;
            b /= 2;
        }
        while (true) {
            if (b % 5 != 0) break;
            b /= 5;
        }
        return b == 1 ? 1 : 2;
    }
    
    public int getGcd(int x, int y) {
        while (true) {
            if (x / y == 0) { 
                return 1;
            } else if (x % y == 0) {
                return y;
            }
            int temp = x % y;
            x = y;
            y = temp;
        }
    }
}