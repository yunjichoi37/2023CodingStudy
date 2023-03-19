package kanghosoo.baekjoon.silver.level4;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Scanner;

public class BOJ_1764 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();
        int M = scan.nextInt();

        HashMap<String, Integer> hm = new HashMap<>();

        ArrayList<String> arrayList = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            hm.put(scan.next(), i);
        }

        for (int i = 0; i < M; i++) {
            String str = scan.next();
            if (hm.containsKey(str)) {
                arrayList.add(str);
            }
        }

        System.out.println(arrayList.size());

        arrayList.sort(new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return o1.compareTo(o2);
            }
        });

        for (int i = 0; i < arrayList.size(); i++) {
            System.out.println(arrayList.get(i));
        }
    }
}
