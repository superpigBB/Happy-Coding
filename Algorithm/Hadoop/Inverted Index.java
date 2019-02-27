/**
 *
 Description
 Create an inverted index with given documents.

 Ensure that data does not include punctuation.

 Have you met this question in a real interview?
 Example
 Given a list of documents with id and content. (class Document)
 Return an inverted index (HashMap with key is the word and value is a list of document ids).
 Example 1:

 Input:
 [
 {
 "id": 1,
 "content": "This is the content of document 1 it is very short"
 },
 {
 "id": 2,
 "content": "This is the content of document 2 it is very long bilabial bilabial heheh hahaha ..."
 },
 ]
 Output:
 {
 "This": [1, 2],
 "is": [1, 2],
 ...
 }
 Example 2:

 Input:
 [
 {
 "id": 1,
 "content": "you are young"
 },
 {
 "id": 2,
 "content": "you are handsome"
 },
 ]
 Output:
 {
 "are": [1, 2],
 ...
 }
 */


/**
 * Definition of OutputCollector:
 * class OutputCollector<K, V> {
 *     public void collect(K key, V value);
 *         // Adds a key/value pair to the output buffer
 * }
 * Definition of Document:
 * class Document {
 *     public int id;
 *     public String content;
 * }
 */
public class InvertedIndex {
    public static class Map {
        public void map(String _, Document value,
                        OutputCollector<String, Integer> output) {
            // Write your code here
            // Output the results into output buffer.
            // Ps. output.collect(String key, int value);
            int id = value.id;
            StringTokenizer tokenizer = new StringTokenizer(value.content);
            while (tokenizer.hasMoreTokens()){
                String word = tokenizer.nextToken();
                output.collect(word, id);
            }
        }
    }

    public static class Reduce {
        public void reduce(String key, Iterator<Integer> values,
                           OutputCollector<String, List<Integer>> output) {
            // Write your code here
            // Output the results into output buffer.
            // Ps. output.collect(String key, List<Integer> value);
            List<Integer> results = new ArrayList<Integer>();
            int previous = -1;
            while (values.hasNext()){
                int now = values.next();
                if(previous != now){
                    results.add(now);
                }
                previous = now;
            }
            output.collect(key, results);
        }
    }
}