
package serializable;

public class Funcionario implements java.io.Serializable{
    public String nome;
    public String endereco;
    public transient int id;
    public int numero;
    public void verificoEmail() {
        System.out.println("Checagem para : " +nome+ " " +endereco);
    }
}
