import java.util.ArrayList;
// import ;

/**
 * Hash
 */
class Hash {

    public static void main(String[] args) {
        java.util.HashMap map = new java.util.HashMap();
        ArrayList a = new ArrayList();
        a.add(10);
        a.add(102132);
        a.add("12312");
        map.put(10, "fdsf");
        map.put(20, "dfasdsf");
        map.put(20, "");
        map.put("dfadfs", 3243);
        map.put(a.hashCode(), 3243);
        System.out.println(map);
        a.add(10);
        map.put(a.hashCode(), 324); 
        System.out.println(map);
        System.out.println(map.get(a.hashCode()));

    }
}