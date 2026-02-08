package udp_java_proxyskel;
import java.net.*;
import java.io.*;

// variante DELEGA: non estendo RealServer ma uso una var IService

public class Skeleton {
    private IService servizio; // rif al vero servizio (DELEGA)
    private int port;

    // costruttore:
    public Skeleton(IService service, int port){
        this.servizio = service;
        this.port = port;
    }

    // funzione per la run dell'ogg skeleton
    public void run_Skeleton(){
        // caso UDP -> utilizzo dei datagram
        DatagramSocket socket = null;
        try{
            // apro la socket sulla porta specifica
            socket = new DatagramSocket(port);
            System.out.println("Socket attivo sulla porta: " + port);

            // preparazione del buffer per la raccolta dati
            byte[] buffer = new byte[1024];
            while(true){
                // ricezione: dichiaro pacchetto e ricevo su di esso dalla socket
                DatagramPacket requestpacket = new DatagramPacket(buffer, buffer.length);
                socket.receive(requestpacket);

                // UNMARSHALLING
                String request = new String(requestpacket.getData(), 0, requestpacket.getLength());
                String valori_estratti[] = request.split(",");
                int num1 = Integer.parseInt(valori_estratti[0]);
                int num2 = Integer.parseInt(valori_estratti[1]);

                // invocazione con delega chiamando il riferimento all'oggetto servizio
                int risultato = this.servizio.somma(num1, num2);

                // MARSHALLING
                String risposta = String.valueOf(risultato);
                byte[] data_risposta = risposta.getBytes();

                // Spedizione: 
                // Ottengo ip/port dal pacchetto dichiarato in precedenza
                InetAddress IpClient = requestpacket.getAddress();
                int portClient = requestpacket.getPort();
                // Costruisco il datagram da spedire
                DatagramPacket responsePacket = new DatagramPacket(data_risposta, data_risposta.length, IpClient, portClient);
                // Spedisco il datagram dalla socket 
                socket.send(responsePacket);
            }
        } catch(Exception e){
            e.printStackTrace();
        }finally{
            if(socket != null){
                socket.close();
            }
        }
    }
    
}
