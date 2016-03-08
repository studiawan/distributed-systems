/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package rmi;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class Message extends UnicastRemoteObject implements MessageInterface {

    public Message() throws RemoteException {        
    }
    
    @Override
    public void Echo(String name) throws RemoteException {
        System.out.println("Echo from client: " + name);
    }
    
}

