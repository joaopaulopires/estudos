
package streams;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.StringWriter;

public class Stream5 {
    public static void main(String [] args)
            throws IOException
    {
        //Cria a string Writer
        StringWriter stringWriter = new StringWriter();
        //Converte  stringWriter para bufferedWriter
        BufferedWriter buffWriter = new BufferedWriter(stringWriter);
        //Escreve "U" para o buffWriter
        buffWriter.write(85);
        //Escreve "N" para o buffWriter
        buffWriter.write(78);
        //Escreve "I" para o buffWriter
        buffWriter.write(73);
        //Escreve "V" para o buffWriter
        buffWriter.write(86);
        //Escreve "E" para o buffWriter
        buffWriter.write(69);
        //Escreve "S" para o buffWriter
        buffWriter.write(83);
        //Escreve "P" para o buffWriter
        buffWriter.write(80);
        buffWriter.flush();
        System.out.println(stringWriter.getBuffer());   
    }
}
