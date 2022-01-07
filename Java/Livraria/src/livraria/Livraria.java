
package livraria;


public class Livraria {

    public static void main(String[] args) {
        LivroFisico livroFisico = new LivroFisico("Robert");
        livroFisico.setNome("Clean Code");
        livroFisico.setValor(50);
        
        LivroDigital livroDigital = new LivroDigital("Robert");
        livroDigital.setNome("Clean Code");
        livroDigital.setValor(30);
        
        CarrinhoDeCompras carrinhoDeCompras = new CarrinhoDeCompras();
        carrinhoDeCompras.adiciona(livroFisico);
        carrinhoDeCompras.adiciona(livroDigital);
        
        System.out.println("Total: " + carrinhoDeCompras.getTotal());
        
        
        
        
    }
    
}
