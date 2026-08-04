from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjList = {}

        wordList.append(beginWord)
        wordList.append(endWord)

        for word in wordList:
            adjList[word] = []
            for i in range(len(word)):
                perm = word[0:i] + '*' + word[i+1:]
                if perm not in adjList:
                    adjList[perm] = [word]
                else:
                    adjList[perm].append(word)
                adjList[word].append(perm)
        

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
                    vst.add(currNode)
                    if currNode == endWord:
                        break
                    for nei in adjList[currNode]:
                        if nei not in vst:
                            q.append(nei)
                dist += 1

        bfs(beginWord)
        return dist//2
            


