/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package testearrays;

import java.util.Arrays;

/**
 *
 * @author 55139
 */
public class TesteArrays {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int vet [] = {3, 4, 6, 34};
        for (int v: vet) {
            System.out.println(v+" ");
        }
        System.out.println(" ");
        int p = Arrays.binarySearch(vet, 68);
        System.out.println("Encotrei o valor na posição "+p);
    }
    
}
