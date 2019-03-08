/**
 Sort integers by Map Reduce framework.
 In the mapper, key is the document id which can be ignored, value is the integers.

 In the reducer, your can specify what the key / value is (this depends on how you implement your mapper class).
 For the output of the reducer class, the key can be anything you want, the value should be ordered.
 (the order is depending on when you output it)

 Example
 Example 1:

 Input:
 1: [14,7,9]
 2: [10,1]
 3: [2,5,6,3]
 4: []
 Output:
 [1,2,3,5,6,7,9,10,14]

 Example 2:

 Input:
 1: [14,7]
 Output:
 [7,14]

 **/


/**
 * Definition of OutputCollector:
 * class OutputCollector<K, V> {
 *     public void collect(K key, V value);
 *         // Adds a key/value pair to the output buffer
 * }
 */
class Element {
    public int row, col, val;
    Element(int row, int col, int val) {
        this.row = row;
        this.col = col;
        this.val = val;
    }
}

public class SortIntegers {

    public static class Map {
        public void map(int _, List<Integer> value,
                        OutputCollector<String, List<Integer>> output) {
            // Write your code here
            // Output the results into output buffer.
            // Ps. output.collect(String key, List<Integer> value);
            Collections.sort(value);
            output.collect("ignore_key", value);
        }
    }

    public static class Reduce {
        public void reduce(String key, List<List<Integer>> values,
                           OutputCollector<String, List<Integer>> output) {
            // Write your code here
            // Output the results into output buffer.
            // Ps. output.collect(String key, List<Integer> value);
            List<Integer> results = new ArrayList<Integer>();
            if (values.size() == 0) {
                output.collect(key, results);
                return;
            }

            int total_size = 0;

            Comparator<Element> ElementComparator = new Comparator<Element>() {
                public int compare(Element left, Element right) {
                    return left.val - right.val;
                }
            };

            Queue<Element> Q = new PriorityQueue<Element>(
                    values.size(), ElementComparator);

            int k = values.size();
            for (int i = 0; i < k; i++) {
                if (values.get(i).size() > 0) {
                    Element elem = new Element(i, 0, values.get(i).get(0));
                    Q.add(elem);
                }
            }

            while (!Q.isEmpty()) {
                Element elem = Q.poll();
                results.add(elem.val);
                if (elem.col + 1 < values.get(elem.row).size()) {
                    elem.col += 1;
                    elem.val = values.get(elem.row).get(elem.col);
                    Q.add(elem);
                }
            }

            output.collect(key, results);
        }
    }
}