import java.util.Scanner;
import java.util.Random;


public class Wordle {

    public static void main(String[] args) {

        final String BG_GREEN = "\u001b[42m";
        final String BG_YELLOW = "\u001b[43m";
        final String RESET = "\u001b[0m";


        System.out.println("WORDLE");

        String[] words = {"apple", "brave", "clown", "dance", "eagle", "fifty", "grape", "house", "ivory", "jolly", "knife", "lemon",
                "mango", "noble", "ocean", "pearl", "queen", "river", "stone", "tiger", "unity", "vivid", "whale",
                "xenon", "yacht", "zebra" };

        int wIndex = (int)(Math.random() * (words.length));
        String correct = words[wIndex].toUpperCase();


        Scanner scanner = new Scanner(System.in);
        String guess = "";

        for (int round = 0; round < 6; round++)
        {
            System.out.print("GUESS: ");
            guess = scanner.nextLine().toUpperCase();

            if (guess.length() != 5) {
                System.out.println("Please enter a 5-letter word.");
                continue;
            }

            for (int i = 0; i < 5; i++) {

                if (guess.substring(i, i+1).equals(correct.substring(i, i+1))) {
                    System.out.print(BG_GREEN + guess.substring(i, i+1) + RESET);
                } else if (correct.indexOf(guess.substring(i, i+1)) > -1) {
                    System.out.print(BG_YELLOW + guess.substring(i, i+1) + RESET);
                } else {
                    System.out.print(guess.substring(i, i+1));
                }
            }
            System.out.println("");

            if (guess.equals(correct)) {
                System.out.println("Correct! You Win");
                break;
            }
        }
        if (!guess.equals(correct)) {
            System.out.println("Wrong! The correct word is: " + correct);

        }
    }
}