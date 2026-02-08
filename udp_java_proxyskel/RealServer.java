package udp_java_proxyskel;

public class RealServer implements IService{
    // implmentazione della logica dei servizi:

    @Override
    public int somma(int num1, int num2){
        System.out.println("REALSERVER: lavoro sui dati\n");
        return num1 + num2;
    }
    
}
