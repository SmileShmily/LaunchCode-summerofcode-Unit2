from tools import Handler
 +
 +class Hello(Handler):
 +
 +    def get(self):
 +        self.render('hello.html', name=self.request.get('name', 'World'))
 +
 +class FizzBuzz(Handler):
 +
 +    def get(self):
 +        n = self.request.get('n', 0)
 +        self.render('fizzbuzz.html', title="FizzBuzz", n=int(n))
 +
 +class ShoppingList(Handler):
 +
 +    def get(self):
 +        items = self.request.get_all("food")
 +        self.render("shopping_list.html", title="Shopping List", items=items)