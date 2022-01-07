
package entradadedados;

import java.util.Scanner;


public class EntradaDeDados {

    
    public static void main(String[] args) {
        
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite o nome do aluno: ");
        String nome = teclado.nextLine(); //método lê uma linha
        System.out.print("Digite a nota do aluno: ");
        float nota = teclado.nextFloat();// método lê um float
        System.out.format("A nota de %s é %.1f \n", nome, nota);
    }
    
}
