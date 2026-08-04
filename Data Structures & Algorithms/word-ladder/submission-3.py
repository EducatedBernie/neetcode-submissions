from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjList = {}

        wordList.append(beginWord)


        for word in wordList:
            adjList[word] = []
            for i in range(len(word)):
                perm = word[0:i] + '*' + word[i+1:]
                if perm not in adjList:
                    adjList[perm] = [word]
                else:
                    adjList[perm].append(word)
                adjList[word].append(perm)

        print(adjList)
        

        # creates the whole network
        dist = 0

        def bfs(node):
            nonlocal dist
            vst = set()
            q = deque()
            q.append(beginWord)
            while q:
                for i in range(len(q)):
                    currNode = q.popleft()
                    if currNode == endWord:
                        return
                    for nei in adjList[currNode]:
                        if nei not in vst:
                            q.append(nei)
                            vst.add(nei)
                dist += 1
            if endWord not in vst:
                return -1

        
        res = bfs(beginWord)
        if res == -1:
            return 0
        return dist//2 + 1
            


