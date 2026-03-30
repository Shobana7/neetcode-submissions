class Node:

    def __init__(self):
        self.children = {}
        self.end_of_word = False
        

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        
        cur.end_of_word = True
        

    def search(self, word: str) -> bool:
        

        def dfs(i, node):
            cur = node

            for j in range(i, len(word)):
                if word[j] == ".":
                    for c in cur.children.values():
                        if dfs(j+1,c):
                            return True
                    return False
                else:
                    if word[j] not in cur.children:
                        return False
                    cur = cur.children[word[j]]
            return cur.end_of_word
        
        return dfs(0,self.root)



        
