// https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        total = []
        for i in range(len(recipes)):
            check = all(item in supplies for item in ingredients[i])
            if check  is True:
                total.append(recipes[i])
                supplies.append(recipes[i])
        return total