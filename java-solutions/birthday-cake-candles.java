import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int height[] = new int[n];
        int max_count = 0, curr_max = Integer.MIN_VALUE;
        for(int height_i=0; height_i < n; height_i++){
            height[height_i] = in.nextInt();
            if (height[height_i] > curr_max) {
                max_count = 1;
                curr_max = height[height_i];
            } else if (height[height_i] == curr_max) {
                max_count++;
            }
        }
        System.out.println(String.format("%d", max_count));
    }
}
