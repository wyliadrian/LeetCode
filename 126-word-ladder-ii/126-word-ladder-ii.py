class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []
        n = len(endWord)
        wordset = set(wordList)
        layer = collections.defaultdict(list)
        # layer: last word in each path is key;
        # the list of all paths ending with that word is value
        layer[beginWord] = [[beginWord]]
        
        while layer:
            if endWord in layer:
                return layer[endWord]
            new_layer = collections.defaultdict(list)
            for word in layer:
                for i in range(n):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new = word[:i] + c + word[i+1:]
                        if new in wordset:
                            new_layer[new] += [path + [new] for path in layer[word]] 
            # keys of new_layer are words that have been met, remove them from wordset
            wordset -= set(new_layer.keys())           
            layer = new_layer
        return []
        