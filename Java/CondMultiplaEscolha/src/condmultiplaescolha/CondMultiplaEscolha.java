
package condmultiplaescolha;

import java.util.Scanner;


public class CondMultiplaEscolha {

   
    public static void main(String[] args) {
        Scanner tec = new Scanner(System.in);
        System.out.println("Quantas pernas? ");
        int perna = tec.nextInt();
        String tipo;
        System.out.println("Isto é um(a) ");
        switch (perna) {
            case 1:
                tipo = "saci";
                break;
            case 2:
                tipo = "Bípede";
                break;
            case 3:
                tipo = "Tripé";
                break;
            case 4:
                tipo = "Quadrúpede";
                break;
            case 6:
                tipo = "Aranha";
                break;
            default:
                tipo = "ET";
        } 
        System.out.println(tipo);
    }
    
}
