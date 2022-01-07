
package serializable;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

public class Serializable {

    public static void main(String[] args) {
        Funcionario e = new Funcionario();
        e.nome = "João Paulo";
        e.endereco = "Rua saturnino de Brito";
        e.id = 203040;
        e.numero = 100;
        try {
            FileOutputStream fileOut = new FileOutputStream("c://Users//55139//funcionario.ser");
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(e);
            out.close();
            fileOut.close();
            System.out.println("Os dados serializados estão salvos no arquivo funcionario.ser");
        } catch (IOException i){
            
        }
    }
}
