
package livraria;

public class CarrinhoDeCompras {
    
    private double total;
    
    public void adiciona(Livro livro){
        System.out.println("Adicionado: " + livro);
        livro.aplicaDescontoDe(0.3);
        
       
        
        total += livro.getValor();
    }
    
    public double getTotal() {
        return total;
        
   
    }
    
    /*public void adiciona(LivroFisico livroFisico){
        System.out.println("Adicionado: " + livroFisico);
    }
    
    public void adiciona(LivroDigital livroDigital){
        System.out.println("Adicionado: " + livroDigital);
    }*/
}
