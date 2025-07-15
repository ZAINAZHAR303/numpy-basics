public class CheckSorted{
    public static void main(){
        int [] arr = {1,3,4,6,8};
        isSorted(arr, 5);
    }
    public static boolean isSorted(int[] arr, int index) {
    if (index == arr.length - 1) return true;
    return arr[index] <= arr[index + 1] && isSorted(arr, index + 1);
}

}