import java.util.*;

class Solution {
    
    class Note {
        float x;
        float y;
        
        public boolean equals(Object o) {
            Note other = (Note) o;
            return this.x == other.x && this.y == other.y;
        }
        
        public int hashCode() {
            return Objects.hash(x, y);
        }
        
        public Note(float x, float y) {
            this.x = x;
            this.y = y;
        }
    }
    
    public static int x = 0;
    public static int y = 0;
    public static int[] limit = {-5, 5};
    public static Set<Note> notes = new HashSet<>();
    public int solution(String dirs) {
        for (String s: dirs.split("")) {
            move(s);
        }
        return notes.size();
    }
    
    public Note move(String direction) {
        switch (direction) {
            case "U":
                if ((y + 1) <= limit[1]) {
                    y += 1;
                    notes.add(new Note((float)x, y - 0.5f));
                }
                break;
            case "D":
                if ((y - 1) >= limit[0]) {
                    y -= 1;
                    notes.add(new Note((float)x, y + 0.5f));
                }
                break;
            case "L":
                if ((x - 1) >= limit[0]) {
                    x -= 1;
                    notes.add(new Note(x + 0.5f, (float)y));
                }
                break;
            case "R":
                if ((x + 1) <= limit[1]) {
                    x += 1;
                    notes.add(new Note(x - 0.5f, (float)y));
                }
                break;
            default:
                break;
        }
        return null;
    }
    
    
}