
package projetoherancacev;

public class ProjetoHerancaCeV {
    
    public static void main(String[] args) {
        
      Aluno a1 = new Aluno();
      a1.setNome("carlos");
      a1.setCurso("word");
      a1.setSexo("m");
      a1.pagarMensalidade();
      
      Bolsista b1 = new Bolsista();
      b1.setMatricula(1111);
      b1.setNome("fabio");
      b1.setBolsa(12.5f);
      b1.setSexo("M");
      b1.pagarMensalidade();
              
    }
    
}
