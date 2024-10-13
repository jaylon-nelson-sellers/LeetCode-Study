class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        """
        @sum: Returns all possible states of the string currentState after one valid move.
        @param: currentState:str a string of + and - representing the flip game
        @return: List[str]: A list of strings of all possible changed values.
        Complexity: O(N)
        """
        
        results = []
        #iterates through the list except the final value
        for i in range(len(currentState)-1):
            #checks if current and next values are saved
            if currentState[i:i+2] == '++':
                #save the result with flipped values
                #[:i] this is all values before the currentState
                #[i+2:] all values after the current and next "++"
                #saves this new string to results
                results.append(currentState[:i] + '--' + currentState[i+2:])
        return results