
package polimorfismosobreposicao;

public class Cachorro extends Mamifero{
   public void enterrarOsso(){
       
   }
    
   public void abanarRabo(){
       
   }

    @Override
    public void locomover() {
        System.out.println("Andando");
    }

    @Override
    public void emitirSom() {
        System.out.println("latindo");
    }
    
    
    
}
