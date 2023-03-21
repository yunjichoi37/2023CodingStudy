package baekjoon.silver.level1;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class BOJ_1931 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int num = scan.nextInt();
        int[][] arr = new int[num][2];

        for (int i = 0; i < num; i++) {
            arr[i][0] = scan.nextInt();
            arr[i][1] = scan.nextInt();
        }

        Arrays.sort(arr, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[1] == o2[1]) {
                    return o1[0] - o2[0];
                }

                return o1[1] - o2[1];
            }
        });

        int count = 0;
        int end_time = 0;

        for (int i = 0; i < num; i++) {
            if (end_time <= arr[i][0]) {
                end_time = arr[i][1];
                count++;
            }
        }

        System.out.println(count);
    }
}
