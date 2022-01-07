
package tarefaimprimir;

public class TesteThread {
    public static void main(String[] args) {
        ThreadTarefaImprimir t1 = new ThreadTarefaImprimir(1, 2000);
        t1.start(); // chama método run()
        ThreadTarefaImprimir t2 = new ThreadTarefaImprimir(2, 1000);
        t2.start();
        ThreadTarefaImprimir t3 = new ThreadTarefaImprimir(3, 900);
        t3.start();
    }
}
