
package univespsemana3;

public class ProfessorConcursado extends Professor{
    
   /* public ProfessorConcursado(int matricula, String nome, int horaTrabalho) {
        super(matricula, nome, horaTrabalho);
    }*/
    public ProfessorConcursado() {
        super();
    }
    
    @Override
    public void calcularSalario(){
        this.setSalario( (this.getHoraTrabalho() * 30) + 1000 );
 
    }
    
    @Override
    public String toString() {
        return ( "Categoria: Professor Concursado" + super.toString());
    }
    /*public void imprimir() {
        System.out.println("Categoria: Professor Concursado");
        System.out.println("Professor(a): " + this.getNome());
        System.out.println("Matrícula: Nº " + this.getMatricula());
        System.out.println("Carga horária: " + this.getHoraTrabalho() + " horas mensais.");
        System.out.println("Salário: R$ " + this.getSalario());
    }*/
}
