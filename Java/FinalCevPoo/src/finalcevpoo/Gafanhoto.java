
package finalcevpoo;

public class Gafanhoto extends Pessoa{
    private String login;
    private int totAssistido;
    
    //Construtor
    public Gafanhoto(String nome, int idade, String sexo, String login) {
        super(nome, idade, sexo);
        this.login = login;
    }
    //Métodos Getter e Setters
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public int getTotAssistido() {
        return totAssistido;
    }

    public void setTotAssistido(int totAssistido) {
        this.totAssistido = totAssistido;
    }
    
    
    public void viuMaisUm(){
        this.setTotAssistido(this.getTotAssistido() + 1);
    }

    @Override
    public String toString() {
        return "Gafanhoto{" + super.toString() + "\n login = " + login + "\n totAssistido = " + totAssistido + '}';
    }
    
    
    
    @Override
    public void ganharExp(){
        
    }

    
    
    
}
