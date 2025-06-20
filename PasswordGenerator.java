import java.util.*;
public class PasswordGenerator
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        Random ra = new Random();
        System.out.print("Enter the length of the password:");
        int pa = sc.nextInt();
        char[] index = {'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'};
        for(int i = 1; i <= pa;i++)
        {
            int r = ra.nextInt(index.length);
            System.out.print(index[r]);
        }
        sc.close();
        
    }
}