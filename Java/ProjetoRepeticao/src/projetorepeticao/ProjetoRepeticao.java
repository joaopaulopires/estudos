/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package projetorepeticao;

import java.util.Scanner;

/**
 *
 * @author 55139
 */
public class ProjetoRepeticao {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int n, s = 0;
        String res;
        Scanner teclado = new Scanner(System.in);
        do {
            System.out.println("Número: ");
            n = teclado.nextInt();
            s += n;
            System.out.println("Continuar? ");
            res = teclado.next();
        } while (res.equals("s"));
        System.out.println("A soma é "+s);
    }
    
}
