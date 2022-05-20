class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.end = True

    def search(self, word: str) -> bool:
        def helper(index, root):
            node = root
            for i in range(index, len(word)):
                c = word[i]

                if c == ".":
                    for child in node.children.values():
                        if helper(i + 1, child):
                            return True
                    return False
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]

            return node.end

        return helper(0, self.root)
