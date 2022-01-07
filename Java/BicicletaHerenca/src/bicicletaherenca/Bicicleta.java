
package bicicletaherenca;
//CLASSE MÃE
/*    class Bicicleta {*/
public class Bicicleta {
    // atributos
    public int disco;
    public int velocidade;

    // Construtor da classe Base
    public Bicicleta(int disco, int velocidade)
    {
	this.disco = disco;
	this.velocidade = velocidade;
    }

    // Alguns métodos da classe
    public void diminuiVelocidade(int diminui)
    {
        velocidade -= diminui;
    }

    public void aumentaVelocidade(int aumenta)
    {
	velocidade += aumenta;
    }

    // Imprime informações sobre a bicicleta
    public String toString() 
    {
	return ("Tamanho do disco da bicicleta é: " + disco + " polegadas \n" + "e a velocidade é " + velocidade + "km/h");
    }
    
}
    

