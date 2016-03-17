import java.util.Properties;
import org.omg.CORBA.Object;
import org.omg.CORBA.ORB;
import org.omg.CORBA.Policy;
import org.omg.PortableServer.POA;
import org.omg.PortableServer.*;
import org.omg.PortableServer.Servant;

public class INSServer {
    public static void main( String args[] ) {
        try {
            Properties properties = System.getProperties( );
            // STEP 1: Set ORBPeristentServerPort property
            // Set the proprietary property to open up a port to listen to
            // INS requests. 
            // Note: This property is subject to change in future releases
            properties.put( "com.sun.CORBA.POA.ORBPersistentServerPort", Integer.toString(1060) );

            // STEP 2: Instantiate the ORB, By passing in the 
            // ORBPersistentServerPort property set in the previous step
            ORB orb = ORB.init( args, properties );

            // STEP 3: Instantiate the Service Object that needs to be published
            // and associate it with RootPOA.
            ServiceImpl servant = new ServiceImpl( );
            POA rootPOA = POAHelper.narrow( orb.resolve_initial_references( "RootPOA" ));
            rootPOA.the_POAManager().activate();
            rootPOA.activate_object( servant );

            // STEP 4: Publish the INS Service using 
            // orb.register_initial_reference( <ObjectKey>, <ObjectReference> 
            // NOTE: Sun private internal API, not part of CORBA 2.3.1.
            // May move as our compliance with OMG standards evolves.
            ((com.sun.corba.se.impl.orb.ORBImpl) orb).register_initial_reference( "PingService", rootPOA.servant_to_reference(servant) );

            System.out.println( "INS Server is Ready..." );
             
            // STEP 5: We are ready to receive requests
            orb.run( );
        } catch ( Exception e ) {
             System.err.println( "Error in setup : " + e );
        }
    } 
}
