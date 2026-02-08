package udp_java_proxyskel;

import udp_java_proxyskel.IService;

public class Client {
    public static void main(String args[]){
        // dichiaro interfaccia e istanzio un server
         String host = "localhost";
         int port = 9000;
        IService service = new Proxy(host, port);
        System.out.println("CLIENT: creo e chiamo il servizio\n");
        // chiamata locale sul servizio
        int result = service.somma(150, 200);
        System.out.println("risultato: "+ result);
    } 
}
