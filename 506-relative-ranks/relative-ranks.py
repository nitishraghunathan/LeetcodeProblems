class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        # Sort scores in descending order
        sorted_scores = sorted(score, reverse=True)
        
        # Map each score to its rank representation
        rank_map = {}
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        
        for idx, s in enumerate(sorted_scores):
            if idx < 3:
                rank_map[s] = medals[idx]
            else:
                rank_map[s] = str(idx + 1)
                
        # Build answer preserving original order
        return [rank_map[s] for s in score]