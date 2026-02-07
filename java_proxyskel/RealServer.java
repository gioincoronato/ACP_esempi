package java_proxyskel;

public class RealServer extends Skeleton {
    // dichiaro il costruttore
    public  RealServer(int port){
        super(port); // passo la porta al costruttore di skeleton
    }
    @Override
    public int somma(int num1, int num2){
        System.out.println("RealServer effettua somma" + num1 + "+" + num2);
        return num1 + num2;
    }
    


public static void main(String args[]){
    RealServer rs = new RealServer(9000);
    rs.runSkeleton();
}
}