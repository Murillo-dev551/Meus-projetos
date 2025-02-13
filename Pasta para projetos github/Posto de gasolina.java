package curso_programacao;

import java.util.Locale;
import java.util.Scanner;

public class Teste {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Locale.setDefault(Locale.US);
		
		int P = sc.nextInt(), gasolina = 0, diesel = 0, alcool = 0, soma = 0;
		
		while (P != 4) {
			if (P == 1) {
				alcool += 1;
			}
			else if (P == 2) {
				gasolina += 1;
			}
			else if (P == 3) {
				diesel += 1;
			}
			P = sc.nextInt();
		}
		System.out.println("MUITO OBRIGADO");
		System.out.println("Alcool : " + alcool);
		System.out.println("Gasolina : " + gasolina);
		System.out.println("Diesel : " + diesel);

	}	
}
