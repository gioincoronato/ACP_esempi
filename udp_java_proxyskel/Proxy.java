package udp_java_proxyskel;

import java.net.*;
import java.io.*;
public class Proxy implements IService{
    // var di classe
    private int port;
    private InetAddress ip;

    // costruttore
    // è necessario passare host e port del server
    public Proxy(String host, int port){
        this.port = port;
        try{
            // trasfromo la string port in un ip
            this.ip = InetAddress.getByName(host);
        } catch(UnknownHostException e){
            e.printStackTrace();
        }
    }
    
    // sovrascrivo il servizio 
    @Override
    public int somma(int num1, int num2){
        // creo la socket di tipo datagram
        DatagramSocket socket = null;
        int risultato = 0; // sarà ritornato al client

        // connessione
        try{
            // apro la socket senza specificare la porta -> ne viene assegnata una a caso
            socket = new DatagramSocket();

            // MARSHALLING -> formato che si aspetta il server
            String messaggio = num1 + "," + num2;
            byte[] data_message = messaggio.getBytes(); // converto in byte il msg

            // spedizione
            // costruzione del pacchetto da spedire
            DatagramPacket requestPacket = new DatagramPacket(data_message, data_message.length, this.ip, this.port);
            // invio del pacchetto sulla socket
            socket.send(requestPacket);
            System.out.println("Proxy: richiesta inviata" + messaggio + "\n");

            // ricezione
            byte[] buffer = new byte[1024]; // preparo un buffer vuoto
            // costruisco il pacchetto per ricevere
            DatagramPacket responsePacket = new DatagramPacket(buffer, buffer.length);
            socket.receive(responsePacket); // ricezione sul pacchetto creato

            // UNMARSHALLING
            // estraggo i dati dal pacchetto e li converto in stringa
            String respString = new String(responsePacket.getData(), 0, requestPacket.getLength());
            // converto la stringa in intero per poterla tornare al client
            risultato = Integer.parseInt(respString.trim());


        } catch(Exception e){
            e.printStackTrace();
        }finally{
            if(socket != null){
                socket.close();
            }
        }

        // ritorno il valore al client
        return risultato;

    }
}
