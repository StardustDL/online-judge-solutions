# longest-palindromic-substring

动态规划。`c[i][j]` 表示子串 `s[i..j]` 是否是回文串。

- 边界：`c[i][i]=true` 和 `c[i][i+1]=s[i]==s[i+1]`
- 从短子串到长子串递推即可。