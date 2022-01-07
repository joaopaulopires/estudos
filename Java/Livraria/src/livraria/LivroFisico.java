
package livraria;

public class LivroFisico extends Livro {
    public LivroFisico(String autor) {
        super(autor);
    }
    
    public double getTaxaDeImpressao() {
        return this.getValor() * 0.05;
    }
}
