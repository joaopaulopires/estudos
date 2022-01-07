
package projetolivro;

import java.util.Calendar;

public class Pessoa {
    private String nome;
    private int idade;
    private String sexo;

    public Pessoa(String nome, int idade, String sexo) {
        this.nome = nome;
        this.idade = idade;
        this.sexo = sexo;
    }
    

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public String getSexo() {
        return sexo;
    }

    public void setSexo(String sexo) {
        this.sexo = sexo;
    }
    
    public void fazerAniver(){
        this.setIdade(this.getIdade()+ 1);
        /*System.out.println("===============Leitor============");
        Calendar ano = Calendar.getInstance();
        int id = ano.get(Calendar.YEAR) - this.getIdade();
        System.out.println("Nome: "+this.getNome());
        System.out.println("Do sexo "+this.getSexo());
        System.out.println("Nasceu em "+id+".");
        System.out.println("=================================")*/;
    }
    
}
