
package univespsemana3;
public class Professor {
    private int matricula;
    private String nome;
    private int horaTrabalho;
    private float salario;
    
   /* public Professor(int matricula, String nome, int horaTrabalho) {
        this.matricula = matricula;
        this.nome = nome;
        this.horaTrabalho = horaTrabalho;
}*/
    public Professor() {
        this.matricula = 0;
        this.nome = null;
        this.horaTrabalho = 0;
    }
    
    public int getMatricula() {
        return matricula;
    }
    
    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }
    
    public String getNome() {
        return nome;
    }
    
    public void setNome(String nome) {
        this.nome = nome;
    }
    
    public int getHoraTrabalho() {
         return horaTrabalho;
     }
    public void setHoraTrabalho(int horaTrabalho) {
        this.horaTrabalho = horaTrabalho;
    }
    
    public float getSalario() {
        return salario;
    }
    
    public void setSalario(float salario) {
        this.salario = salario;
    }
    public void calcularSalario(){
        this.setSalario( this.getHoraTrabalho() * 30 );
    }
    
    public String toString() {
        return ("\nProfessor(a): " + this.getNome() + 
                "\nMatrícula: Nº " + this.getMatricula() +
                "\nCarga horária: " + this.getHoraTrabalho() + " horas mensais." +
                "\nSalário: R$ " + this.getSalario());
    }
    /*public void imprimir() {
        System.out.println("Professor(a): " + this.getNome());
        System.out.println("Matrícula: Nº " + this.getMatricula());
        System.out.println("Carga horária: " + this.getHoraTrabalho() + " horas mensais.");
        System.out.println("Salário: R$ " + this.getSalario());
    }*/
}

/*class ProfessorConcursado extends Professor{
    //Atributo específico da subclasse
    private String categoria;
    
    
    /*public ProfessorConcursado(Professor){
        super(matricula, nome, horaTrabalho)
            //invocação do construtor da classe base
        
            //
            this.categoria = "Professor Concursado";
    }*/
    
    

