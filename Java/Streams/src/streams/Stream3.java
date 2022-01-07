
/*package streams;

import java.io.BufferedOutputStream;
import java.io.ByteArrayOutputStream;

public class Stream3 {
    public static void main(String[] args) 
        throws Exception
    {
        //Cria byteArrayOutputStream
        ByteArrayOutputStream byteArrayOutStr = new ByteArrayOutputStream();
        //Converte byteArrayOutputStream para bufferedOutputStream
        BufferedOutputStream buffOutputStr = new BufferedOutputStream(byteArrayOutStr);
        for (int i = 65; i < 91; i++) {
            //escrev para buffOutputStr
            buffOutputStr.write(i);
        }
        buffOutputStr.flush();
        for (
                byte by:byteArrayOutStr.toByteArray()) {
            //Converte bytre para caracter
            char ch = (char) by;
            System.out.println(ch);
        }
        
    }
}*/
