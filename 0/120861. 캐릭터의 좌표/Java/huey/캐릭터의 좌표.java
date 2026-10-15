class Solution {
    public int h;
    public int v;
    public int leftLimit;
    public int rightLimit;
    public int upLimit;
    public int downLimit;
    
    public int[] solution(String[] keyinput, int[] board) {
        leftLimit = - (board[0] / 2);
        rightLimit = board[0] / 2;
        upLimit = board[1] / 2;
        downLimit = - (board[1] / 2);
        
        for (String s: keyinput) {
            move(s);
        }
        
        return new int[] { h, v };
    }
    
    public void move(String input) {
        switch (input) {
            case "left":
                if (h - 1 >= leftLimit) h -= 1;
                break;
            case "right":
                if (h + 1 <= rightLimit) h += 1;
                break;
            case "up":
                if (v + 1 <= upLimit) v += 1;
                break;
            case "down":
                if (v - 1 >= downLimit) v -= 1;
                break;
            default:
                break;
        }
    }
}