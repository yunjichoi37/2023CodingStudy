package baekjoon.silver.level1;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_1697 {
    static int N;
    static int K;
    static int[] visit = new int[100001];
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        N = scan.nextInt();
        K = scan.nextInt();

        if (N == K) {
            System.out.println(0);
        } else {
            bfs(N);
        }
    }

    static void bfs(int num) {

        Queue<Integer> Q = new LinkedList<>();
        Q.add(num);
        visit[num] = 0;

        while (!Q.isEmpty()) {
            int now = Q.poll();

            for (int i = 0; i < 3; i++) {
                int next;

                if (i == 0) {
                    next = now + 1;
                } else if (i == 1) {
                    next = now - 1;
                } else {
                    next = now * 2;
                }
                if (next >= 0 && next < visit.length && visit[next] == 0) {
                    Q.add(next);
                    visit[next] = visit[now] + 1;
                }

                if (next == K) {
                    System.out.println(visit[next]);
                    return;
                }

            }
        }
    }
}
