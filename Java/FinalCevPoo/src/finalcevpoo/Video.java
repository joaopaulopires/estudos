
package finalcevpoo;
public class Video implements AcoesVideo{
    private String titulo;
    private float avaliacao;
    private int views;
    private int curtidas;
    private boolean reproduzindo;
    
    //Construtor
    public Video(String titulo) {
        this.titulo = titulo;
        this.avaliacao = 1;
        this.views = 0;
        this.curtidas = 0;
        this.reproduzindo = false;
    }
    
    //Métodos Acessores
    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public float getAvaliacao() {
        return avaliacao;
    }

    public void setAvaliacao(float avaliacao) {
        int nova;
        nova = (int) ((this.avaliacao + avaliacao) / this.views);
        this.avaliacao = nova;
    }

    public int getViews() {
        return views;
    }

    public void setViews(int views) {
        this.views = views;
    }

    public int getCurtidas() {
        return curtidas;
    }

    public void setCurtidas(int curtidas) {
        this.curtidas = curtidas;
    }

    public boolean getReproduzindo() {
        return reproduzindo;
    }

    public void setReproduzindo(boolean reproduzindo) {
        this.reproduzindo = reproduzindo;
    }
    
    //Métodos abstratos
    @Override
    public void play() {
        //this.reproduzindo = true;
        this.setReproduzindo(true);
        System.out.println("========= Play > =========");
    }

    @Override
    public void pause() {
        this.reproduzindo = false;
        System.out.println("========= Pause || =========");
    }

    @Override
    public void like() {
        //this.curtidas ++;
        this.setCurtidas(this.getCurtidas() + 1);
        System.out.println("========= Curtiu ! =========");
    }

    @Override
    public String toString() {
        return "Video{" + "titulo = " + titulo + "\n avaliacao = " + 
                avaliacao + "\n views = " + 
                views + "\n curtidas = " + 
                curtidas + "\n reproduzindo = " + 
                reproduzindo + '}';
    }
    
    
    
}
