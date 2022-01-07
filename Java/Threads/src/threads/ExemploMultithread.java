
package threads;

public class ExemploMultithread {
    public static void main(String [] args) {
        int n = 8; // número de threads
        for (int i = 0; i < n; i++) {
            Thread t = new Thread(new MultiThreading());
            t.start();
        }
    }
}