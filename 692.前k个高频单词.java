/*
 * @lc app=leetcode.cn id=692 lang=java
 *
 * [692] 前K个高频单词
 */

// @lc code=start
import java.util.ArrayList;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.List;
class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        HashMap<String, Integer> map = new HashMap<>();
        for(String word: words){
            map.put(word, map.getOrDefault(word, 0)+1);
        }
        PriorityQueue<WordFreq> queue = new PriorityQueue<>();
        for(String key:map.keySet()){
            WordFreq wordFreq = new WordFreq(map.get(key), key);
            queue.offer(wordFreq);
        }
        List<String> list = new ArrayList<>();
        while(k>0){
            list.add(queue.poll().word);
            k--;
        }
        return list;

    }

    public static class WordFreq implements Comparable<WordFreq>{
        int freq;
        String word;
        
        WordFreq(int freq, String word){
            this.freq = freq;
            this.word = word;
        }

        public int compareTo(WordFreq other){
            if(this.freq == other.freq){
                return this.word.compareTo(other.word);
            }
            return other.freq - this.freq;
        }
    }
}
// @lc code=end

