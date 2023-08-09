/*
 * @lc app=leetcode.cn id=297 lang=java
 *
 * [297] 二叉树的序列化与反序列化
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.util.LinkedList;
import java.util.Arrays;
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        //序列化好写，只要考虑空节点就行
        if(root==null)return "#";
        return Integer.toString(root.val) + "," + serialize(root.left) + "," + serialize(root.right);
        
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        //解码肯定也是递归
        String[] arr = data.split(",");
        LinkedList<String> queue = new LinkedList<>(Arrays.asList(arr));
        return helper(queue);
        
        
    }

    public TreeNode helper(LinkedList<String> queue){
        String val = queue.pollFirst();
        if("#".equals(val)) return null;
        TreeNode node = new TreeNode(Integer.parseInt(val));
        node.left = helper(queue);
        node.right = helper(queue);
        return node;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));
// @lc code=end

