package baekjoon.gold.level4;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_9019 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int num = scan.nextInt();
        for (int i = 0; i < num; i++) {
            int a = scan.nextInt();
            int b = scan.nextInt();

            String[] command = new String[10000];
            Arrays.fill(command, "");

            boolean[] visit = new boolean[10000];

            Queue<Integer> Q = new LinkedList<>();

            visit[a] = true;
            Q.add(a);

            while (!Q.isEmpty() && !visit[b]) {
                int now = Q.poll();

                int D = D(now);
                int S = S(now);
                int L = L(now);
                int R = R(now);

                if (!visit[D]) {
                    Q.add(D);
                    visit[D] = true;
                    command[D] = command[now] + "D";
                }

                if (!visit[S]) {
                    Q.add(S);
                    visit[S] = true;
                    command[S] = command[now] + "S";
                }

                if (!visit[L]) {
                    Q.add(L);
                    visit[L] = true;
                    command[L] = command[now] + "L";
                }

                if (!visit[R]) {
                    Q.add(R);
                    visit[R] = true;
                    command[R] = command[now] + "R";
                }
            }

            System.out.println(command[b]);
        }
    }

    public static int D(int num) {
        return (2 * num) % 10000;
    }

    public static int S(int num) {
        if (num == 0) {
            return 9999;
        } else {
            return num - 1;
        }
    }

    public static int L(int num) {
        int d1 = num / 1000;
        return (num - (d1 * 1000)) * 10 + d1;
    }

    public static int R(int num) {
        int d4 = num % 10;
        return ((num - d4) / 10) + d4 * 1000;
    }
}
