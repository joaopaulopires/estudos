
package serializable;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;

public class Desserializa {
    public static void main(String [] args) {
        Funcionario e;
        try 
        {
            try (FileInputStream fileln = new FileInputStream("c://Users//55139//funcionario.ser");
            ObjectInputStream in = new ObjectInputStream(fileln)) {
                e = (Funcionario)in.readObject();
            }
        } catch(IOException i){
            return;
        } catch (ClassNotFoundException c) {
            System.out.println("Classe Funcionário não encontrada!");
            return;
        }
            System.out.println("Funcionário desserializado...");
            System.out.println("Nome: " +  e.nome);
            System.out.println("Endereço: "+ e.endereco);
            System.out.println("ID: " + e.id);
            System.out.println("Número: " +e.numero);
    }
}
