package python_orientado_objeto;
import java.util.Map;

class Conta {
    //atributos
    private int numero;
    private String titular;
    private double saldo;
    private double limite;

    //construtor
    Conta(int numero, String titular, double saldo, double limite){
        this.numero = numero;
        this.titular = titular;
        this.saldo = saldo;
        this.limite = limite;
        
    }

    void extrato(){
        System.out.println("saldo de " + this.saldo + "do titular" + this.titular);
    }

    void deposita(double valor) {
        this.saldo += valor;

    }
    
    private boolean podeSacar(double valor_a_sacar) {
        double valorDisponivelaSacar = this.saldo + this.limite;
        return valor_a_sacar <= valorDisponivelaSacar;
    }

    boolean saca(double valor) {
        if(this.podeSacar(valor)) {
            this.saldo -= valor;
            return true;
        }else {
            System.out.println("O valor" + valor + "passou do limite");
        }
        return false;
    }

    void transfere(double valor, Conta conta){
        this.saca(valor);
        this.deposita(valor);
    }

    public double getLimite() {
        return limite;
    }

    public void setLimite(double limite) {
        this.limite = limite;
    }

    public int getNumero() {
        return numero;
    }

    public String getTitular() {
        return titular;
    }

    public double getSaldo() {
        return saldo;
    }

    public static String codigo(){
        return "001";
    }

    public static Map codigos(){
        return Map.of("BB", "001", "caixa", "124", "bradesco", "142");
    }
    
}

/*Conta contaDoFabio = new Conta(123, "fabio", 55.0, 1000.0);
contaDoFabio.depositaa(100.0)*/
