
package streams;


import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Stream4 {
    public static void main(String [] args)
            throws FileNotFoundException, IOException
    {
        //lê a stream
        FileReader fileReader = new FileReader("C://Users//55139//Documents//exercicio.txt");
        
        //Converte fileReader para bufferedReader
        BufferedReader buffReader = new BufferedReader(fileReader);
        while (buffReader.ready()) {
            //Lê e imprimi caracteres um a um 
            System.out.println("Caractere4: "+(char)buffReader.read());
        }
    }
}
