package DZZ2;
import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        System.out.println("Введите количество дисков");
        Scanner scanner = new Scanner(System.in);
        int q = scanner.nextInt();
        hanoi(q, 1, 2, 3);
        
    }

  static void hanoi(int q, int from, int to, int buf){
    if (q==0) return;
    hanoi(q-1,from,buf,to);
    System.out.println(from + " -> " + to);
    hanoi(q-1,buf,to,from);
  }
}3