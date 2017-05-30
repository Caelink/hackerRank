import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] arr = new int[5];
        for(int arr_i=0; arr_i < 5; arr_i++){
            arr[arr_i] = in.nextInt();
        }
        
        boolean natural = arr[0] < arr[1];
        int min = natural ? 0 : 1, max = natural ? 1 : 0;
        for (int i = 2; i < 5; i++) {
            if (arr[i] < arr[min]) {
               min = i;
            } else if (arr[i] > arr[max]) {
               max = i;
            }
        }
        long min_sum = 0, max_sum = 0;
        for (int i = 0; i < 5; i++) {
            if (i != max) {
                min_sum += arr[i];
            }
            if (i != min) {
                max_sum += arr[i];
            }
        }
        System.out.println(String.format("%d %d", min_sum, max_sum));
    }
}
