import java.util.Scanner;

/**
 * WayTooLongWords
 */
public class WayTooLongWords {

    public static void main(String[] args) {
        String word;

        int length;
        Scanner scanner = new Scanner(System.in);
        length = Integer.valueOf(scanner.nextLine());
        

        for (int i = 0; i < length; i++) {
            word = scanner.nextLine();
            if (word.isEmpty()) {
                break;
            }
        
            if (word.length() > 10) {
                word = String.valueOf(word.charAt(0)) + String.valueOf(word.length() - 2) + String.valueOf(word.charAt(word.length()-1));
            }
        System.out.println(word);
            
        }

        
         scanner.close();
    }
}