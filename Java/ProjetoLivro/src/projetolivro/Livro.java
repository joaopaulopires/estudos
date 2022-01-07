
package projetolivro;


public class Livro implements Publicacao{
    private String livro;
    private String autor;
    private int totPaginas;
    private int pagAtual;
    private boolean aberto;
    private Pessoa leitor;

    public Livro(String livro, String autor, int totPaginas, Pessoa leitor) {
        this.livro = livro;
        this.autor = autor;
        this.totPaginas = totPaginas;
        this.leitor = leitor;
        this.pagAtual = 0;
        this.aberto = false;
    }

    public String getLivro() {
        return livro;
    }

    public void setLivro(String livro) {
        this.livro = livro;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public int getTotPaginas() {
        return totPaginas;
    }

    public void setTotPaginas(int totPaginas) {
        this.totPaginas = totPaginas;
    }

    public int getPagAtual() {
        return pagAtual;
    }

    public void setPagAtual(int pagAtual) {
        this.pagAtual = pagAtual;
    }

    public boolean getAberto() {
        System.out.println(""+aberto);
        return aberto;
    }

    public void setAberto(boolean aberto) {
        this.aberto = aberto;
    }

    public Pessoa getLeitor() {
        return leitor;
    }

    public void setLeitor(Pessoa leitor) {
        this.leitor = leitor;
    }

    
    public String detalhes() {
        return "Livro{" + "livro=" + livro + 
                "\n, autor=" + autor + "\n, totPaginas=" 
                + totPaginas + "\n, pagAtual=" + this.getPagAtual() + 
                "\n, aberto=" + aberto + "\n, leitor=" + leitor.getNome()
                + " idade = " + leitor.getIdade() 
                + ", sexo = " + leitor.getSexo() + "}";
    }
    
    
        public void detalhes(Pessoa leitor) {
        System.out.println("=========Livro==========");
        System.out.println("Livro: "+this.getLivro());
        System.out.println("Autor: "+this.getAutor());
        System.out.println(this.getTotPaginas()+" páginas.");
        System.out.println("Página atual: "+this.getPagAtual());
        System.out.println("Aberto: "+this.getAberto());
        System.out.println("Leitor: "+leitor.getNome()+". "+leitor.getIdade()+" anos.");
        System.out.println("========================");
    }

    @Override
    public void abrir() {
        System.out.println("+++++++++++++++abrir()+++++++++++++++++");
        if (aberto) {
            System.out.println("O livro já está aberto na página "+this.getPagAtual());
        } else {
            this.setAberto(true); //= true;
            System.out.println("Você abriu o livro. Página atual de leitura: "+this.getPagAtual());
            System.out.println("Tenha uma boa leitura!");
        }
        System.out.println("================================");
    }

    @Override
    public void fechar() {
        System.out.println("+++++++++++++++fechar()+++++++++++++++++");
        if (aberto){
            this.setAberto(false); // false;
            System.out.println("Você parou sua leitura na página "+this.getPagAtual());
        }else {
            System.out.println("O livro já está fechado.");
        }
        System.out.println("================================");
    }

    @Override
    public void folhear() {
        System.out.println("+++++++++++++++folhear()+++++++++++++++++");
        if (aberto) {
            System.out.println("Páginas: ");
            for(int i = 0; i < this.getTotPaginas(); i++){
                if (i == 50 || i == 100 || i == 150 || i == 200 || i == 250 || i == 300 || i == 350 || i == 400 ){
                    System.out.println(i+" - ");
                } else {
                    System.out.print(i+" - ");
                }
            }System.out.print(this.getTotPaginas());
        } else {
            System.out.println("O livro está fechado. Para folhear, você precisa abrir.");
        }
    }

    @Override
    
    public void avancarPag() {
        System.out.println("+++++++++++++++avancarPag()+++++++++++++++++");
        this.setPagAtual(this.getPagAtual() +1);
        System.out.println("Página "+this.getPagAtual());
    }

    @Override
    public void voltarPag() {
        System.out.println("+++++++++++++++voltarPag()+++++++++++++++++");
        this.setPagAtual(this.getPagAtual() -1);
        System.out.println("Página "+this.getPagAtual());
    }
}
