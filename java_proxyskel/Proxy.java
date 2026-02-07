package java_proxyskel;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.*;
import java.io.*;

public class Proxy implements IService {

    // class var
    private String host;
    private int port;

    // costruttore di classe
    public Proxy(String host, int port){
        this.host = host;
        this.port = port;
    }
    
    @Override
    public int somma(int num1, int num2){
        int risultato = 0;

        try{
            // creazione della socket -> include connect
            Socket socket = new Socket(this.host, this.port);

            // creo canale per scrivere verso il server
            PrintWriter client_data_writer = new PrintWriter(socket.getOutputStream(), true);
           
            // creo canale per leggere dal server:
            // ottengo i byte grezzi dal server
            InputStream server_data_stream = socket.getInputStream();
            // codifico il flusso
            InputStreamReader server_data = new InputStreamReader(server_data_stream);
            // metto i dati nel buffer per leggerlo successivamente
            BufferedReader server_data_buffer = new BufferedReader(server_data);

            // INVIO DEI DATI [num1,num2]
            client_data_writer.println(num1 + "," + num2);

            // RICEZIONE DATI e conversione
            String risposta = server_data_buffer.readLine();
            if(risposta != null){
                risultato = Integer.parseInt(risposta);
            }
            socket.close();
        
        } catch(IOException e){
            System.out.println(e.getMessage());
        }

        return risultato;

    }
}
