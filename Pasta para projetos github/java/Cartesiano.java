package curso_programacao;

import java.util.Locale;
import java.util.Scanner;

public class Teste {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Locale.setDefault(Locale.US);
		
		int x, y;
		x = sc.nextInt();
		y = sc.nextInt();
		
		while (x != 0 && y != 0) {
			if (x < 4 && y < 4) {
				System.out.println("Primeiro");
			}
			else if (x > -4 && x < 0 && y < 4) {
				System.out.println("Segundo");
			}
			else if (x > -4 && x < 0 && y > -4 && y < 0) {
				System.out.println("Terceiro");
			}
			else if (x < 4 && y > -4 && y < 0 ) {
				System.out.println("Quarto");
			}
			x = sc.nextInt();
			y = sc.nextInt();

		}
		sc.close();

	}	
}
