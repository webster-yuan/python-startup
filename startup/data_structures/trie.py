class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]
            
        # 把最后一个节点的是否为最后一个节点的标注为设置为 True
        node.is_end = True

    def search(self, prefix: str) -> bool:
        node = self._find_node(prefix)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def _find_node(self, s: str):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None

            node = node.children[ch]

        return node


def test_trie():
    trie = Trie()

    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.starts_with("app") is True

    trie.insert("app")
    assert trie.search("app") is True

    print("Trie test passed")


if __name__ == "__main__":
    test_trie()
