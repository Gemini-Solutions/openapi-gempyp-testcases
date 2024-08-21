from gempyp.gemPyp import Gempyp
 
obj = Gempyp()
 
obj.config = "C:\\Users\\ayush.gupta1\\Desktop\\Performance_Test_GemEco\\openapi-gempyp-testcases\\open-apis.xml,C:\\Users\\ayush.gupta1\\Desktop\\Performance_Test_GemEco\\openapi-gempyp-testcases\\testcases.xml"

if __name__ == "__main__":
    obj.runner()