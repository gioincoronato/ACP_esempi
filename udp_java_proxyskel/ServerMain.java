package udp_java_proxyskel;

public class ServerMain {
    public static void main(String args[]){
        // creazione del servizio reale
        IService servizio_reale = new RealServer();

        // creazione dello skeleton
        int port = 9000;

        Skeleton skeleton = new Skeleton(servizio_reale, port);
        // passo allo skeleton la porta ed il servizio reale creato
        // avvio lo sekeleton
        skeleton.run_Skeleton();

    }
    
}
