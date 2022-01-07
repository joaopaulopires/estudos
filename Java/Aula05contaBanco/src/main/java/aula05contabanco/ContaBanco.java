package aula05contabanco;
public class ContaBanco {
    public int numConta;
    protected String tipo;
    private String dono;
    private float saldo;
    private boolean status;
    
    public void estadoAtual() {
        System.out.println("-----------------");
        System.out.println("Conta: " + this.getNumConta());
        System.out.println("Tipo: " + this.getTipo());
        System.out.println("Nome: " + this.getDono());
        System.out.println("Saldo: " + this.getSaldo());
        System.out.println("Status: " + this.getStatus());
    }
    
     public void abrirConta(String t) {
        this.setTipo(t);
        this.setStatus(true);
        if ( t == "CC") {
            this.setSaldo(50f);
        } else if ( t == "CP") {
            this.setSaldo(150f);
        }
       
    }
     
    public void fecharConta() {
        if (this.getSaldo() > 0) {
            System.out.println("Seu saldo atual é de R$  " + this.getSaldo());
            System.out.println("Para encerrar a conta, você deve sacar todo o valor");
        } else if (this.getSaldo() < 0) {
            System.out.println("Seu saldo é de R$ " + this.getSaldo());
            System.out.println("Para fechar a conta, sua dívida deve ser liquidada.");          
        } else {
            this.setStatus(false);
            System.out.println("Sua conta foi encerrada.");
        }
    }
        
    public void depositar(float v) {
        if (this.getStatus()) {
            this.setSaldo(this.getSaldo() + v);
            System.out.println("Deposíto realizado na conta de " + this.getDono());
        } else {
            System.out.println("Impossível depositar em uma conta fechada.");
        }
    }
    
    public void sacar(float v) {
        if (this.getStatus()) {
            if (this.getSaldo() >= v){
                this.setSaldo(this.getSaldo() - v);
                System.out.println("Saque realizado na conta de " + this.getDono());
            } else {
                System.out.println("Saldo insuficiente para saque.");
            }
        } else{
            System.out.println("Impossível sacar de uma conta fechada.");
        }   
    }
    
     public void pagarMensal(){
        int v = 0;
         if (this.getTipo() == "CC") {
             v = 12;
         } else if (this.getTipo() == "CP"){
             v = 20;
         } if (this.getStatus()) {
             this.setSaldo(this.getSaldo() - v);
             System.out.println("Mensalidade paga por " + this.getDono());
         } else {
             System.out.println("Impossível pagar mensalidade de conta fechada.");
         }
    }
    public ContaBanco() {
       
       this.status = false;
       this.saldo = 0f;
    }
    
    public int getNumConta() {
       return this.numConta;
    }
   
    public void setNumConta(int num) {
       this.numConta = num;
    }
   
    public String getTipo() {
       return tipo;
    }
   
    public void setTipo(String tipoConta) {
       this.tipo = tipoConta;
    }
    public String getDono() {
       return this.dono;
    }
   
    public void setDono(String nome) {
       this.dono = nome;
    }
   
    public float getSaldo() {
       return this.saldo;
    }
   
    public void setSaldo(float saldo) {
       this.saldo = saldo;
    }
    
    public boolean getStatus() {
        return status;
    }
    
    public void setStatus(boolean status) {
        this.status = status;
    }
  
   
   
    public void imprimir() {
       System.out.println("Conta número :" + this.numConta);
       System.out.println("Tipo de conta: " + this.tipo);
       System.out.println("Nome: " + this.dono);
       System.out.println("Saldo: R$" + this.saldo);
    }

}
