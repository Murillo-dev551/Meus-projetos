import java.util.Scanner;
import java.util.Locale;

public class teste3 {

	public static void main(String[] args) {
		Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		
		int N = 3; //Quantidade de vezes que pode se repetir o loop
		
		double n, n2, n3, peso,peso2,peso3; //Declaração das variáveis
		
		for (int i=0; i<N;i++) { //Processo normal
			n = sc.nextDouble();
			n2 = sc.nextDouble();
			n3 = sc.nextDouble();
			peso = 2; 
			peso2 = 3;
			peso3 = 5;
			
			double multi1 = n * peso; //Aqui começa a multiplicação de cada valor por seu peso
			double multi2 = n2 * peso2;
			double multi3 = n3 * peso3;
			
			double somaresultados = multi1 + multi2 + multi3; //A soma dos resultados da multiplicação
			double somapesos = peso + peso2 + peso3; //Soma dos pesos
			double somatotal = somaresultados / somapesos; //Divisão dos dois resultados anteriores
			
			System.out.printf("Resultado : %.1f", somatotal); //Exibição do resultado
		}
		
		sc.close();
	}
}
