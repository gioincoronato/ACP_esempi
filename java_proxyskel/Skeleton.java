package java_proxyskel;
import java.net.*;
import java.io.*;

public abstract class Skeleton implements IService {
    protected int port;

    // costruttore
    public Skeleton(int port){
        this.port = port;
    }

    public void runSkeleton(){
        System.out.println("Server avviato alla porta: " + port );

        // in java per usare le funzioni di rete è necessario gestire le eccezzioni
        try{
            // creazione del server socket: fa bind e listen (50 deafult) insieme
            ServerSocket serverSocket = new ServerSocket(port);
            System.out.println("Skeleton in ascolto, port: " + port);

            while(true){

                // accetto la socket del client
                Socket socket_client = serverSocket.accept();
                System.out.println("SKELETON: Socket client accetta");
                
                //  INIZIO LETTURA
                // ricevo flusso grezzo dalla socket del client
                InputStream client_data_stream = socket_client.getInputStream();

                // analizzo il flusso grezzo
                InputStreamReader client_data = new InputStreamReader(client_data_stream);
                
                // istanza di un oggetto per la lettura dal client
                BufferedReader client_data_read = new BufferedReader(client_data);
                // FINE LETTURA

                // INIZIO SCRITTURA
                // istanza di un oggetto per la scrittura sul client
                PrintWriter client_data_writer = new PrintWriter(socket_client.getOutputStream(), true);
                
                // legge la riga del messaggio
                String message = client_data_read.readLine();
                System.out.println("Messaggio letto: "+ message);

                if(message != null){
                    // split dei messaggi
                    String[] numeri_letti = message.split(",");
                    int num1 = Integer.parseInt(numeri_letti[0]);
                    int num2 = Integer.parseInt(numeri_letti[1]);
                    int risultato = this.somma(num1, num2);

                    // invio effetivo della risposta
                    client_data_writer.println(risultato);

                }
                
                // chiudo la connessione
                socket_client.close();
                
            }
 
        }
        catch(IOException e){
            System.out.println("errore di rete" + e.getMessage());
        }
    }
}
