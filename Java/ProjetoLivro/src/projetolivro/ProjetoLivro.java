
package projetolivro;

public class ProjetoLivro {

    public static void main(String[] args) {
        Pessoa pessoa[] = new Pessoa[5];
        Livro livro[] = new Livro[5];
        //teste.fazerAniver();
        pessoa[0] = new Pessoa("Joao", 20, "M");
        pessoa[1] = new Pessoa("Maria", 40, "F");
        pessoa[2] = new Pessoa("Paulo", 60, "M");
        pessoa[3] = new Pessoa("Ingrid", 80, "F");
        pessoa[4] = new Pessoa("Tadeu", 100, "M");
        
        
        livro[0] = new Livro("Livro1", "Autor1", 100, pessoa[0]);
        livro[1] = new Livro("Livro2", "Autor2", 200, pessoa[1]);
        livro[2] = new Livro("Livro3", "Autor3", 300, pessoa[2]);
        livro[3] = new Livro("Livro4", "Autor4", 400, pessoa[3]);
        livro[4] = new Livro("Livro5", "Autor5", 500, pessoa[4]);
        
        System.out.println(livro[0].detalhes());
        //System.out.println(".."+ livro[0].getAberto());
        

        livro[0].abrir();
        livro[0].avancarPag();
        livro[0].avancarPag();
        livro[0].avancarPag();
        livro[0].avancarPag();
        livro[0].voltarPag();
        livro[0].folhear();
        System.out.println(livro[0].detalhes());
        
//System.out.println(".."+ livro[0].getAberto());
        //livro[0].abrir();

// livro[0].fechar();
        
        //livro[2].fechar();
        /*livro[2].abrir();
        //livro[4].folhear();
        livro[2].avancarPag();
        livro[2].abrir();
        livro[2].avancarPag();
        livro[2].avancarPag();
        livro[2].avancarPag();
        livro[2].voltarPag();
        //livro[2].folhear();
        livro[2].fechar();*/
        
    }
    
}
