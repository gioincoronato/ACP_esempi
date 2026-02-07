package java_proxyskel;



public class Client {
    public static void main(String args[]){
        String host = "localhost";
        int port = 9000;
        IService server = new Proxy(host, port);
        int risultato = server.somma(port, port);
        System.out.println("risultato: " +risultato);
    }
}
