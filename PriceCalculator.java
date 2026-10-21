// Optional Java example: calculate an order total using the same per-unit pricing idea.
import java.util.Scanner;

public class PriceCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Shubham Farm - Order Price Calculator");
        System.out.print("Enter price per unit (INR): ");
        double price = input.nextDouble();
        System.out.print("Enter quantity: ");
        double quantity = input.nextDouble();

        if (price < 0 || quantity < 0) {
            System.out.println("Price and quantity cannot be negative.");
        } else {
            System.out.printf("Total: ₹%.2f%n", price * quantity);
        }
        input.close();
    }
}