/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
 var minWindow = function(s, t) {
    let l=0, n=t.length;
    const ht = {}
    const vis = {}
    let cnt = 0
    let dist = 1/0
    let a,b
    for (let i=0; i<n; i++){
        let c = t[i];
        vis[c] = 0
        if (ht[c]) ht[c]++;
        else {
            ht[c] = 1;
            cnt += 1
        }
    }
    
    for (let r=0; r<s.length; r++){
        let c = s[r];
        if (ht[c]){
            vis[c]++;
            if (vis[c] == ht[c]){
                cnt--
            }
        }
        if (cnt == 0){
            while ((!ht[s[l]] || ht[s[l]] < vis[s[l]]) && l<r){
                vis[s[l]]--;
                l++;
            }
            if (r-l < dist){
                dist = r-l
                a=l; b=r;
            }
        }
    }
    
    return s.slice(a,b+1);
};