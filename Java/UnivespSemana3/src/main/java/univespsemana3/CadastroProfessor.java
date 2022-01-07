package univespsemana3;
public class CadastroProfessor {
    public static void main(String[] args) {
        /*Professor p1 = new Professor(22, "joao", 100);
        p1.calcularSalario();
        p1.imprimir();
        System.out.println("------------------------------------------");
        System.out.println("------------------------------------------");
        ProfessorConcursado p2 = new ProfessorConcursado(22, "joao", 100);
        p2.calcularSalario();
        p2.imprimir();*/
        
        Professor p1 = new Professor();
        p1.setMatricula(22);
        p1.setNome("joao");
        p1.setHoraTrabalho(100);
        p1.calcularSalario();
        System.out.println(p1.toString());
        //p1.imprimir();
        System.out.println("------------------------------------------");
        System.out.println("------------------------------------------");
        ProfessorConcursado p2 = new ProfessorConcursado();
        p2.setMatricula(22);
        p2.setNome("tadeu");
        p2.setHoraTrabalho(100);
        p2.calcularSalario();
        System.out.println(p2.toString());
        //p2.imprimir();
        System.out.println("------------------------------------------");
        System.out.println("------------------------------------------");
        ProfessorHorista p3 = new ProfessorHorista();
        p3.setMatricula(23);
        p3.setNome("Olavo");
        p3.setHoraTrabalho(100);
        p3.calcularSalario();
        System.out.println(p3.toString());
        //p3.imprimir();
    }
    
}
