package baekjoon.silver.level1;

import java.util.Scanner;

public class BOJ_1992 {

    static char[][] image;

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();

        image = new char[n][n];

        for (int i = 0; i < n; i++) {
            String line = scan.next();
            for (int j = 0; j < n; j++) {
                image[i][j] = line.charAt(j);
            }
        }

        String compressed = compress(0, 0, n);

        System.out.println(compressed);
    }

    static String compress(int x, int y, int size) {

        // 모든 값이 같은 경우
        if (isSame(x, y, size)) {
            return Character.toString(image[x][y]);
        }

        // 4개의 영역으로 분할하여 각각 압축
        int half = size / 2;
        String upperLeft = compress(x, y, half);
        String upperRight = compress(x, y + half, half);
        String lowerLeft = compress(x + half, y, half);
        String lowerRight = compress(x + half, y + half, half);

        // 압축된 결과를 괄호로 묶어서 반환
        return "(" + upperLeft + upperRight + lowerLeft + lowerRight + ")";
    }

    static boolean isSame(int x, int y, int size) {
        char color = image[x][y];
        for (int i = x; i < x + size; i++) {
            for (int j = y; j < y + size; j++) {
                if (color != image[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }
}
