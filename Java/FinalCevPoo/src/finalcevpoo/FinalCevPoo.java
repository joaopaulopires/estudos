
package finalcevpoo;

public class FinalCevPoo {

    public static void main(String[] args) {
        Video v[] = new Video[5];
        v[0] = new Video("POO");
        v[1] = new Video("PHP");
        v[2] = new Video("Java");
        
        Gafanhoto g[] = new Gafanhoto[2];
        g[0] = new Gafanhoto("JP", 21, "m", "c@anal");
        g[1] = new Gafanhoto("Mary", 30, "f", "c@anal");
        
        Visualizacao vis[] = new Visualizacao[5];
        vis[0] = new Visualizacao(g[0], v[2]);
        System.out.println(vis[0].toString());
        vis[0] = new Visualizacao(g[0], v[0]);
        System.out.println(vis[0].toString());
        vis[0] = new Visualizacao(g[1], v[0]);
        System.out.println(vis[0].toString());
        /*System.out.println(g.toString());
        g.viuMaisUm();
        System.out.println(g.toString());
        
        System.out.println(v[0].toString());
        v[0].play();
        v[0].like();
        System.out.println(v[0].toString());*/
    }
    
}
