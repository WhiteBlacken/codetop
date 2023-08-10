/*
 * @lc app=leetcode.cn id=990 lang=java
 *
 * [990] 等式方程的可满足性
 */

// @lc code=start
class Solution {
    public boolean equationsPossible(String[] equations) {
        UF uf = new UF(26);
        //先把等于的聚类
        for(String eq:equations){
            if(eq.charAt(1)=='='){
                int a = (int)eq.charAt(0) - (int)'a';
                int b = (int)eq.charAt(3) - (int)'a';
                uf.union(a, b);
            }
        }
        for(String eq:equations){
            if(eq.charAt(1)=='!'){
                int a = (int)eq.charAt(0) - (int)'a';
                int b = (int)eq.charAt(3) - (int)'a';
                if(uf.connected(a, b))return false;
            }
        }
        return true;
    }
}
class UF{
    private int[] parent;
    private int[] size;

    public UF(int n){
        parent = new int[n];
        size = new int[n];
        for(int i=0;i<n;i++){
            parent[i] = i;
        }
        for(int i=0;i<n;i++){
            size[i] = 1;
        }
    }

    public int find(int x){
        if(parent[x]!=x)parent[x] = find(parent[x]);
        return parent[x];
    }

    public void union(int x,int y){
        int root_x = find(x);
        int root_y = find(y);
        if(root_x==root_y)return;
        if(size[root_x]<size[root_y]){
            int tmp = root_x;
            root_x = root_y;
            root_y = tmp;
        }
        parent[root_y] = root_x;
        size[root_x] += size[root_y];
    }

    public boolean connected(int x, int y){
        return find(x) == find(y);
    }

}
// @lc code=end

