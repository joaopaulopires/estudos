/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package funcao01;

/**
 *
 * @author 55139
 */
public class Fatorial {
    int num = 0;
    int fat = 1;
    String formula = "";

    public void setValor(int n) {
        num = n;
        int f = 1;
        String s = "";
        for (int c = n; c > 1; c--) {
            f *= c;
            s += c + " X ";
        }
        s += "1 = ";
        fat = f;
        formula = s;
    }
    public String getFormula(){
        return formula;
    }
    public int getFatorial() {
        return fat;
    }
}
