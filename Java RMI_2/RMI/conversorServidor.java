import java.rmi.*;
import java.rmi.server.UnicastRemoteObject;

public class conversorServidor extends UnicastRemoteObject implements conversor {
    protected conversorServidor() throws RemoteException {
        super();
    }

    @Override
    public double euroParaReal(double valorEuro) throws RemoteException {
        return valorEuro * 5.41;
    }

    @Override
    public double realParaEuro(double valorReal) throws RemoteException {
        return valorReal * 0.18;
    }

    @Override
    public double dolarParaReal(double valorDolar) throws RemoteException {
        return valorDolar * 5.0;
    }

    @Override
    public double realParaDolar(double valorReal) throws RemoteException {
        return valorReal * 0.2;
    }

    public static void main(String[] args) {
        try {
         conversorServidor server = new conversorServidor();
            System.out.println("Servidor de conversão de moeda pronto...");
            Naming.rebind("rmi://127.0.0.1:11099/ConversorMoeda", server);
        } catch (Exception e) {
            System.out.println("Problema ao iniciar o servidor: " + e);
        }
    }
}