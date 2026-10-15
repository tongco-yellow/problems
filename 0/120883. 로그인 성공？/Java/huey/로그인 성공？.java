import java.util.*;

class Solution {
    public String solution(String[] id_pw, String[][] db) {
        String password = Arrays.stream(db)
            .filter(row -> row[0].equals(id_pw[0]))
            .map(row -> row[1])
            .findFirst()
            .orElse("");
        if (password.equals("")) {
            return "fail";
        } else if (password.equals(id_pw[1])) {
            return "login";
        } else {
            return "wrong pw";
        }
    }
}