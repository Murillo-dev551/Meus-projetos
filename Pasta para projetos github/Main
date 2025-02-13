package estruturacondicional;

import java.util.Locale;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		
		int s;
		System.out.println("Digite sua senha a seguir: ");
		s = sc.nextInt();
		
		while ( s != 2002) {
			System.out.println("Senha inválida.");
			System.out.println("Digite novamente a senha a seguir: ");
			s = sc.nextInt();
			if (s == 2002) {
				System.out.println("Acesso permitido.");
				break;
			}
		}
		
		sc.close();
	}

}
