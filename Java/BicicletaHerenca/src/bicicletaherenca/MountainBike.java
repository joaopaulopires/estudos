
package bicicletaherenca;

// Classe Derivada/Filha
class MountainBike extends Bicicleta {

	// Um atributo específico desta classe
	public int altAssento;

	// Construtor da classe filha
	public MountainBike(int disco, int velocidade, int startAltura)
	{
		// invocação do construtor da classe base (Bicicelta)
		super(disco, velocidade);
		altAssento = startAltura;
	}

	// Este método é específico da subclasse
	public void setaAltura(int valor)
	{
		altAssento = valor;
	}

	// overriding o método toString() de Bicicleta, para escreve mais informações
	@Override public String toString()
	{
		return (super.toString() + "\n A alutura do assento é: " + altAssento + " cm");
	}
}

