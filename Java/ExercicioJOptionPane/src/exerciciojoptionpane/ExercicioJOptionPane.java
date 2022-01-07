
package exerciciojoptionpane;

import javax.swing.JOptionPane;
public class ExercicioJOptionPane {

    
    public static void main(String[] args) {
        // TODO code application logic here
        int n, s = 0;
     do {
        n = Integer.parseInt(JOptionPane.showInputDialog(null, 
                "<html><h1>Número:</h1><hr> </br> </br> <em>(Valor 0 interrompe)</em></html>"));
        s += n;
        //JOptionPane.showMessageDialog(null, "Número: "+ n);
     } while (n!= 0 );
     JOptionPane.showMessageDialog(null,"Mostre resultado: "+s);
    }
    
}
