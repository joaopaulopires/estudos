
package projetoherancacev;

public class Bolsista extends Aluno{
    private float bolsa;
    
    public void renovarBolsa(){
        System.out.println("Bolsa renovada"+ this.getNome() +this.getNome());
    }

    public float getBolsa() {
        return bolsa;
    }

    public void setBolsa(float bolsa) {
        this.bolsa = bolsa;
    }
    

    @Override
    public void pagarMensalidade() {
        System.out.println(this.getNome() +" é bolsista. Pagamento facilitado");
    }
    
}
