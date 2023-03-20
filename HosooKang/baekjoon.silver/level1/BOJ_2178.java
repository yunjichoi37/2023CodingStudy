package baekjoon.silver.level1;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_2178 {
    static int[] dx = {-1, 0, 0, 1};
    static int[] dy = {0, 1, -1, 0};
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int M = scan.nextInt();

        int[][] maps = new int[N][M];
        int[][] visit = new int[N][M];

        for (int i = 0; i < N; i++) {
            String str = scan.next();
            for (int j = 0; j < M; j++) {
                maps[i][j] = Character.getNumericValue(str.charAt(j));
            }
        }

        bfs(maps, visit);

        System.out.println(visit[N-1][M-1] + 1);
    }

    public static class Point{
        public int x, y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void bfs(int[][] maps, int[][] visit) {
        Queue<Point> Q = new LinkedList<>();
        Q.offer(new Point(0, 0));

        maps[0][0] = 0;

        while (!Q.isEmpty()) {
            Point tmp = Q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = tmp.x + dx[i];
                int ny = tmp.y + dy[i];
                if (nx >= 0 && nx <= maps.length-1 && ny >= 0 && ny <= maps[0].length-1 && maps[nx][ny] == 1) {
                    maps[nx][ny] = 0;
                    Q.offer(new Point(nx, ny));
                    visit[nx][ny] = visit[tmp.x][tmp.y] + 1;
                }
            }
        }
    }
}
