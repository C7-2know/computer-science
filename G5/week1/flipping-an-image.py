class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            for j in range(math.ceil(len(image[0])/2)):
                if image[i][j]==image[i][len(image[0])-j-1]:
                    image[i][j]=1-image[i][j]
                    if len(image[0])-j-1!=j:
                        image[i][len(image[0])-j-1]=1-image[i][len(image[0])-j-1]
        return image