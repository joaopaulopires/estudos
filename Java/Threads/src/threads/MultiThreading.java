
package threads;

public class MultiThreading implements Runnable{
    @Override
    public void run() {
        try {
            //Mostra a thread em execução
            System.out.println("Thread " +Thread.currentThread().getId() + " está executando.");
        } catch (Exception e) {
            //lança uma exceção
            System.out.println("Exceção gerada");
        }
    }
}
