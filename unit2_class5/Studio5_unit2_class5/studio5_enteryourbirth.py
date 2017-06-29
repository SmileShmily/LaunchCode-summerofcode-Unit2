import webapp2

form = """
<form method="post">
what is your birthday
<br>

<label>Month<input type="text" name="month"></label>

<label>Day<input type="text" name="day"></label>

<label>Year<input type="text" name="year"></label>
<div style="color: red">%(error)s</div>

 <br>
 <br>
 <input type="submit">
</form>
"""

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']


def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day < 32 and day > 0:
            return day
        else:
            return 0


def valid_month(month):
    if (month):
        month = month.capitalize()
        if month in months:
            return month
        else:
            return 0


def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year < 2020 and year > 1880:
            return year
        else:
            return 0


class MainPage(webapp2.RequestHandler):
    def write_form(self, error=""):
        self.response.out.write(form % {"error": error})

    def get(self):
        self.write_form()

    def post(self):
        user_month = valid_month(self.request.get('month'))
        user_day = valid_day(self.request.get('day'))
        user_year = valid_year(self.request.get('year'))

        if not (user_day and user_month and user_year):
            self.write_form("That doesn't look valid to me, friend.")
        else:
            self.response.out.write("Thanks! That's a totally valid day!")


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)