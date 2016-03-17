// Implementation of Service interface
public class ServiceImpl extends ServicePOA {
    public String ping(String message) {
        System.out.println( "PingService.ping called..." + message );        
        return message;
    }
}
