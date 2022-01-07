
package livraria;
public class Livro {
    
    private String nome;
    private double valor;
    private String isbn;
    private String autor;
    
    public Livro (String autor) {
        this.autor = autor;
    }
        
     public boolean aplicaDescontoDe (double porcentagem) {
        if (porcentagem > 0.3) {
            return false;
        } 
        System.out.println("Aplicando desconto no livro Físico.");
        this.valor -= this.valor * porcentagem;
        return true;
    }
   
    public String getNome() {
        return nome;
    }
    
    public void setNome(String nome) {
        this.nome = nome;
    }
    
    public double getValor() {
        return valor;
    }
    
    public void setValor(double valor) {
        this.valor = valor;
    }
    
    public String getIsbn() {
        return isbn;
    }
    
    public void setIsbn(String isbn){
        this.isbn = isbn;
    }
    
    public String getAutor() {
        return autor;
    }
    
    public void setAutor(String autor) {
        this.autor = autor;
    }
}

