import java.util.*;
public class PasswordGenerator
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        Random ra = new Random();
        System.out.print("Enter the length of the password:");
        int pa = sc.nextInt();
        char[] index = {'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'};
        char[] number = {'1','2','3','4','5','6','7','8','9','0'};
        char[] signs = {'!','@','#','$','%','&','?','/'};
        System.out.print(index[ra.nextInt(index.length)]);
        for(int i = 2; i <= pa;i++)
        {
            int ArraySelector = ra.nextInt(1,4); 
            if(ArraySelector == 1)
            {
                int chr = ra.nextInt(number.length);
                System.out.print(number[chr]);
            }
            else if(ArraySelector == 2)
            {
                int chr = ra.nextInt(index.length);
                System.out.print(index[chr]);
            }
            else if(ArraySelector == 3)
            {
                int chr = ra.nextInt(signs.length);
                System.out.print(signs[chr]);
            }
        }
        sc.close();
    }
}