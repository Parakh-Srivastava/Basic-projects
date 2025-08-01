import java.util.Scanner;
import java.util.Random;
public class NumbGuess 
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        Random ra = new Random();
        
        System.out.print("Enter the range of the gameplay : ");
        int range = sc.nextInt();
        System.out.print("Enter the number of guesses : ");
        int guesses = sc.nextInt();
        int WinNum = ra.nextInt(0, range);

        boolean winCondition = false;
        for(int i = 1; i <= guesses; i++)
        {
            System.out.print("Guess "+ i +") = ");
            int Userguess = sc.nextInt();

            if(Userguess == WinNum)
            {
                System.out.println("You win !!");
                winCondition = true;
                break;
            }
            else if(Userguess > WinNum)
            {
                System.out.println("You guessed a higher number");
            }
            else
            {
                System.out.println("You guessed a smaller number");
            }
        }
        if(winCondition == false)
        {
            System.out.println("The number was " + WinNum + ".");
        }
        else 
        {
            System.out.println("The number was indeed "+ WinNum + ".");
        }
        sc.close();
    }  
}
