class Sample():
    def classSetup(self):
        print("will run once before evry test suite")

    def test_m1(self):
        print("method1")
        assert True
    def test_m2(self):
        print("method2")

