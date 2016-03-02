/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package main;

import rmi.Message;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Main {
    
    private void startServer(){
        try {        
            /*
             * register server in port 5000 and bind as service named "Echo"
             */
            Registry registry = LocateRegistry.createRegistry(5000);                        
            registry.rebind("Echo", new Message());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }      
        System.out.println("Server is ready");
    }
    
    public static void main(String[] args) {
        Main main = new Main();
        main.startServer();
    }
}
