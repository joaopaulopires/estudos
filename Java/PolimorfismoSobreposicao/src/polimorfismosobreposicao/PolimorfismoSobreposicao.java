
package polimorfismosobreposicao;

public class PolimorfismoSobreposicao {

    
    public static void main(String[] args) {
        Mamifero m = new Mamifero();
        Reptil r = new Reptil();
        Peixe p = new Peixe();
        Ave a = new Ave();
        
        Canguru c = new Canguru();
        Cachorro ca = new Cachorro();
        
       c.locomover();
       ca.locomover();
       c.emitirSom();
       ca.emitirSom();
        
     
        
    }
    
}
