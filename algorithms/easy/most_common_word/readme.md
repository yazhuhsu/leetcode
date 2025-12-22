## 819. Most Common Word
### Rules
- Given a `paragraph` string and a list of `banned` words
- Find the most frequently occurring word that is NOT banned
- Words are case-insensitive
- Punctuation marks (`,`, `!`, `?`, `'`, `;`, `.`) should be treated as word separators
- Return the result in lowercase

### Ideas
- Replace all punctuation with spaces
    ```go
    replacer := strings.NewReplacer(
        ",", " ",
        "!", " ",
        "?", " ",
        "'", " ",
        ";", " ",
        ".", " ",
    )
    sentences := replacer.Replace(paragraph)
    ```
- Split into words and count frequency (case-insensitive)
    ```go
    words := strings.Split(sentences, " ")
    wordMap := make(map[string]int, len(words))
    for _, word := range words {
        if word == "" {
            continue
        }
        wordMap[strings.ToLower(word)] += 1
    }
    ```
- Create banned word lookup
    ```go
    bannedMap := make(map[string]bool, len(banned))
    for _, word := range banned {
        bannedMap[strings.ToLower(word)] = true
    }
    ```
- Find maximum frequency word that's not banned
    ```go
    max, maxWord := 0, ""
    for word, count := range wordMap {
        if count > max && !bannedMap[word] {
            max = count
            maxWord = word
        }
    }
    ```

### Walkthrough (paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"])
```
sentences = replacer.Replace(paragraph)
└─ "Bob hit a ball  the hit BALL flew far after it was hit "

words = strings.Split(sentences, " ")
└─ ["Bob", "hit", "a", "ball", "", "the", "hit", "BALL", "flew", "far", "after", "it", "was", "hit", ""]

wordMap = make(map[string]int)
for _, word := range words:
├─ word="Bob": wordMap["bob"]=1
├─ word="hit": wordMap["hit"]=1
├─ word="a": wordMap["a"]=1
├─ word="ball": wordMap["ball"]=1
├─ word="": skip (empty)
├─ word="the": wordMap["the"]=1
├─ word="hit": wordMap["hit"]=2
├─ word="BALL": wordMap["ball"]=2
├─ word="flew": wordMap["flew"]=1
├─ word="far": wordMap["far"]=1
├─ word="after": wordMap["after"]=1
├─ word="it": wordMap["it"]=1
├─ word="was": wordMap["was"]=1
├─ word="hit": wordMap["hit"]=3
└─ word="": skip (empty)

bannedMap = {"hit": true}

max, maxWord = 0, ""
for word, count := range wordMap:
├─ word="bob", count=1: count > 0 && !banned → max=1, maxWord="bob"
├─ word="hit", count=3: count > 1 && banned → skip
├─ word="a", count=1: count ≤ 1 → skip
├─ word="ball", count=2: count > 1 && !banned → max=2, maxWord="ball"
├─ word="the", count=1: count ≤ 2 → skip
├─ word="flew", count=1: count ≤ 2 → skip
├─ word="far", count=1: count ≤ 2 → skip
├─ word="after", count=1: count ≤ 2 → skip
├─ word="it", count=1: count ≤ 2 → skip
└─ word="was", count=1: count ≤ 2 → skip

return maxWord = "ball"
```

### Result
- Output: "ball" (appears 2 times, highest among non-banned words)
