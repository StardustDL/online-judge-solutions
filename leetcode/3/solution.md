# longest-substring-without-repeating-characters

从左到右扫描字符串 `s[i]`，维护

- 一个哈希表 `H`，`H[c]` 表示字符 `c` 最后一次出现的位置
- 当前以 `s[i]` 为右端点的无重复极长子串左端点 `l[i]`

若 `s[i]` 出现过，为保证 `l` 性质，使用 `max(H[c]+1,l[i-1])` 得到 l[i]。进而答案为 `i-l[i]+1` 的最大值。
