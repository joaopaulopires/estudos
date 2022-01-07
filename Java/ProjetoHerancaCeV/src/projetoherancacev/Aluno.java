
package projetoherancacev;

public class Aluno extends Pessoa {
    //Herança para Diferença
    //Subclasse de Pessoa
    //Especialização de Pessoa
    private int matricula;
    private String curso;
    
    public void pagarMensalidade(){
        System.out.println("Pagando mensalidade de Aluno");
    }

    public int getMatricula() {
        return matricula;
    }

    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }

    public String getCurso() {
        return curso;
    }

    public void setCurso(String curso) {
        this.curso = curso;
    }

    @Override
    public String toString() {
        return "\nAluno{" + "matricula=" + matricula + ", curso=" + curso + '}';
    }
    
    
}
