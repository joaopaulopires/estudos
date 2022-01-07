
package univespsemana3;

public class ProfessorHorista extends Professor{
    
    public ProfessorHorista() {
        super();
    }
    
    @Override
    public void calcularSalario() {
        this.setSalario( this.getHoraTrabalho() * 27 );
    }
    
    @Override
    public String toString() {
        return("Categoria: Professor Horista" + super.toString());
    }
    /*public void imprimir() {
        System.out.println("Categoria: Professor Horista");
        System.out.println("Professor(a): " + this.getNome());
        System.out.println("Matrícula: Nº " + this.getMatricula());
        System.out.println("Carga horária: " + this.getHoraTrabalho() + " horas mensais.");
        System.out.println("Salário: R$ " + this.getSalario());
    }*/
}
