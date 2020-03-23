############################## my code ###########################
def designerPdfViewer(h, word):
    measures = [h[ord(i) - ord('a')] for i in word]
    
    return len(word) * max(measures)
########################## end of my code ########################