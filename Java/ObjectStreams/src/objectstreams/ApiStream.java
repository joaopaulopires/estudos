
package objectstreams;


import java.util.Arrays;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class ApiStream {
    public static void main(String args[]) {
        //Cria uma lista de inteiros
        List<Integer>numList1 = Arrays.asList(10, 20, 30, 40);
        
        //demonstração do método map()
        List<Integer>multiplica = numList1.stream().map(y->y*y).collect(Collectors.toList());
        System.out.println("Resultado da multiplicação: "+multiplica);
        
        //Criar uma lista de Strings
        List<String>nomes = Arrays.asList("UNIVESP", "USP", "UNICAMP", "UNESP");
        
        //Uso do método filter()
        List<String>resultado = nomes.stream().filter(s->s.startsWith("U")).collect(Collectors.toList());
        System.out.println("Resultado do filtro: " +resultado);
        
        //uso do método sorted()
        List<String>mostra = nomes.stream().sorted().collect(Collectors.toList());
        System.out.println("Resultado com o método sorted(): "+ mostra);
        
        //cria uma Lista de Inteiros
        List<Integer>numList2 = Arrays.asList(100, 200, 300, 400, 500);
        
        //método collect() retorna um conjunto
        Set<Integer>multiplicaSet = numList2.stream().map(x->x*x).collect(Collectors.toSet());
        System.out.println("Resultado com o método collect(): " + multiplicaSet);
        
        //demonstração do método forEach()
        numList2.stream().map(x->x*x).forEach(y->System.out.println(y));
    }
}
