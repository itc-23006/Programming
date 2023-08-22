class Person:
    def __init__(self, name="", nationality="", birth="", address=""):
        self.name = name
        self.nationality = nationality
        self.birth = birth
        self.address = address

    def show_attributes(self):
        print("名前:", self.name)
        print("国籍:", self.nationality)
        print("生まれた年:", self.birth)
        print("住んでいる所:", self.address)


# インスタンスを作成し、属性を表示する
heroine = Person("清少納言", "日本", "966", "梨壺(東北地方のどこか)")
heroine.show_attributes()
