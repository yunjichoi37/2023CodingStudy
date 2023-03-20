package baekjoon.silver.level2;

import java.util.Scanner;

public class BOJ_1541 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String next = scan.next();

        int sum = Integer.MAX_VALUE;
        String[] sub = next.split("-");

        for (int i = 0; i < sub.length; i++) {
            int tmp = 0;

            String[] add = sub[i].split("\\+");

            for (int j = 0; j < add.length; j++) {
                tmp += Integer.parseInt(add[j]);
            }

            // 첫번째는 양수일 수도 있으니
            if (sum == Integer.MAX_VALUE) {
                sum = tmp;
            } else {
                sum -= tmp;
            }
        }
        System.out.println(sum);
    }
}
