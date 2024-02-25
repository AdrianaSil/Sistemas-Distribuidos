import java.rmi.Naming;

public class conversorCliente {
    private static conversor conversorService = null;

    public static void main(String[] args) {
        try {
            conversorService = (conversor) Naming.lookup("rmi://127.0.0.1:11099/ConversorMoeda");

            double real = 2;
            double dolar = 2;
            double euro = 2;
            
            //real em euro
            System.out.println("--> R$ " + real + " equivalente a € " + conversorService.realParaEuro(real));

            //euro em real
            System.out.println("--> € " + euro + " equivalente a R$" + conversorService.euroParaReal(euro));

            //real em dolar
            System.out.println("--> R$ " + real + " equivalente a $ " + conversorService.realParaDolar(real));

            //dolar em real
            System.out.println("--> $ " + dolar + " equivalente a R$ " + conversorService.dolarParaReal(dolar));

        } catch (Exception e) {
            System.out.println("Problema com o cliente: " + e);
        }
    }
}