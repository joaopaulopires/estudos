/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package exerepita;

import javax.swing.JOptionPane;


public class ExeRepita {

   
    public static void main(String[] args) {
     // TODO code application logic here
     int n, s = 0;
     do {
        n = Integer.parseInt(JOptionPane.showInputDialog(null, 
                "<html>Número: </br>(Valor 0 interrompe)</html>"));
        s += n;
        //JOptionPane.showMessageDialog(null, "Número: "+ n);
     } while (n!= 0 );
     JOptionPane.showMessageDialog(null,"Mostre resultado: "+s);
    }
    
}
