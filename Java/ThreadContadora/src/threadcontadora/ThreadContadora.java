
package threadcontadora;

public class ThreadContadora implements Runnable{
    
    Thread mythread;
    
    ThreadContadora() {
        mythread = new Thread(this, "minha thread runnable");
        System.out.println("MInha thread criada: " +mythread);
        mythread.start();
    }
    
    public void run() {
        try {
            for(int i = 0; i < 10; i++) {
                System.out.println("Contador: "+i);
                Thread.sleep(1000);
            }
        } catch (InterruptedException e) {
            System.out.println("Minha thread interrompida.");
        }
        System.out.println("Método run() da thread filha finalizado.");
    }

    public static void main(String args[]) {
        ThreadContadora cnt = new ThreadContadora();
        try {
            while (cnt.mythread.isAlive()) {
                System.out.println("Thread principal estará ativa enquanto a thread filha esteja ativa");
                Thread.sleep(1000);
            }
        } catch (InterruptedException e) {
            System.out.println("A thread principal foi interrompida");
        }
        System.out.println("Método run() da thread principal finalizado.");
    }
}
