class WordFilter {
    private static final int ALPHABET_LENGTH = 'z' - 'a' + 1;
    private final Node[] rootPref = new Node[ALPHABET_LENGTH];
    private final Node[] rootSuff = new Node[ALPHABET_LENGTH];

    public WordFilter(String[] words) {
        for (int i = 0; i < words.length; i++) {
            addToTrie(words[i], i, rootPref, false);
            addToTrie(words[i], i, rootSuff, true);
        }
    }

    private static void addToTrie(String word, int index, Node[] trie, boolean reversed) {
        Node[] currLvl = trie;
        Node[] lastLvl = trie;
        char c = 0;
        int wordLen = word.length();
        if (reversed) {
            for (int i = 0; i < wordLen; i++) {
                c = word.charAt(wordLen - i - 1);
                int charIndex = c - 'a';
                if (currLvl[charIndex] == null) {
                    currLvl[charIndex] = new Node(c);
                }
                lastLvl = currLvl;
                currLvl = currLvl[charIndex].children;
            }
        } else {
            for (int i = 0; i < wordLen; i++) {
                c = word.charAt(i);
                int charIndex = c - 'a';
                if (currLvl[charIndex] == null) {
                    currLvl[charIndex] = new Node(c);
                }
                lastLvl = currLvl;
                currLvl = currLvl[charIndex].children;
            }
        }

        lastLvl[c - 'a'].index = index;
    }

    public int f(String prefix, String suffix) {

        var pref = findInTrie(prefix, rootPref);
        var suf = findInTrie(new StringBuilder(suffix).reverse().toString(), rootSuff);

        return intersection(pref, suf);
    }

    private int intersection(Set<Integer> pref, Set<Integer> suf) {
        int max = -1;
        for (var e : pref) {
            if (suf.contains(e) && e > max) max = e;
        }
        return max;
    }

    private Set<Integer> findInTrie(String prefix, Node[] root) {
        int rememberLast = -1;
        for (int i = 0; i < prefix.length(); i++) {
            if (root[prefix.charAt(i) - 'a'] == null) return new HashSet<>();
            rememberLast = root[prefix.charAt(i) - 'a'].index;
            root = root[prefix.charAt(i) - 'a'].children;
        }

        HashSet<Integer> result = new HashSet<>();
        result.add(rememberLast);
        collectWords(root, result);
        return result;
    }

    private void collectWords(Node[] root, HashSet<Integer> result) {
        for (int i = 0; i < ALPHABET_LENGTH; i++) {
            var child = root[i];
            if (child != null) {
                if (child.children != null)
                    collectWords(child.children, result);
                if (child.index != -1)
                    result.add(child.index);
            }
        }
    }

    private static class Node {
        char c;
        Node[] children;
        int index = -1;

        public Node(char c) {
            this.c = c;
            this.children = new Node[ALPHABET_LENGTH];
        }
    }
}
