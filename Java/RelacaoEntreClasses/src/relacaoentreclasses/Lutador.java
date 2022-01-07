
package relacaoentreclasses;


public class Lutador implements TorneioLutador{
    private String nome;
    private String nacionalidade;
    private int idade;
    private float altura;
    private float peso;
    private String categoria;
    private int vitorias;
    private int derrotas;
    private int empates;
    
    public Lutador (String no, String na, int id, float al, 
            float pe, int vi, int de, int em ) {
        this.nome = no;
        this.nacionalidade = na;
        this.idade = id;
        this.altura = al;
        this.setPeso(pe);
        this.vitorias = vi;
        this.derrotas = de;
        this.empates = em;
        
        
    };

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getNacionalidade() {
        return nacionalidade;
    }

    public void setNacionalidade(String nacionalidade) {
        this.nacionalidade = nacionalidade;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public float getAltura() {
        return altura;
    }

    public void setAltura(float altura) {
        this.altura = altura;
    }

    public float getPeso() {
        return peso;
    }

    public void setPeso(float peso) {
        this.peso = peso;
        setCategoria();
    }

    public String getCategoria() {
        return categoria;
    }

    public void setCategoria() {
        if (peso < 52.2) {
            this.categoria = "Inválido";
        } else if (peso <= 70.3) {
            this.categoria = "Leve";
        } else if (peso <= 83.9){
            this.categoria = "Médio";
        } else if (peso <= 120.2) {
            this.categoria = "Pesado";
        } else {
            this.categoria = "Inválido";
        }
    }

    public int getVitorias() {
        return vitorias;
    }

    public void setVitorias(int vitorias) {
        this.vitorias = vitorias;
    }

    public int getDerrotas() {
        return derrotas;
    }

    public void setDerrotas(int derrotas) {
        this.derrotas = derrotas;
    }

    public int getEmpates() {
        return empates;
    }

    public void setEmpates(int empates) {
        this.empates = empates;
    }

    
    
    @Override
    public void apresentar() {
        System.out.println("===================================");
        System.out.println("Lutador: " +this.getNome());
        System.out.println("origem: " +this.getNacionalidade());
        System.out.println(this.getIdade()+ " anos.");
        System.out.println(this.getAltura()+" m de altura");
        System.out.println("Pesando "+this.getPeso()+ "kg");
        System.out.println("Ganhou "+this.getVitorias()+ " lutas,");
        System.out.println("Teve "+this.getDerrotas()+" derrotas.");
        System.out.println("E "+this.getEmpates()+" empates.");
        System.out.println("===================================");
    }

    @Override
    public void status() {
        System.out.println("===================================");
        System.out.print(this.getNome());
        System.out.println(" é um peso "+this.getCategoria());
        System.out.println(this.getVitorias()+" vitórias.");
        System.out.println(this.getDerrotas()+" derrotas.");
        System.out.println(this.getEmpates()+ " empates.");
        System.out.println("===================================");
    }

    @Override
    public void ganharLuta() {
        setVitorias(getVitorias() + 1);
    }

    @Override
    public void perderLuta() {
        setDerrotas(getDerrotas() + 1);
    }

    @Override
    public void empatarLuta() {
        setEmpates(getEmpates() + 1);
    }
    
}
