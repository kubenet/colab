from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__)
app.secret_key = 'my-super-secret-phrase-I-dont-tell-this-to-nobody'
dict_score = {'Alex': 10, 'Anton': 20}
lst_code = ['111', '222', '333', '444']


class VerificationForm(FlaskForm):
    name = StringField()
    code = StringField()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = VerificationForm()

    if request.method == 'POST':
        # получаем данные
        name = form.name.data
        code = form.code.data
        if code in lst_code:  # если такой код существует
            score = dict_score.setdefault(name, 0)  # если такого пользователя не существует, тогда создаем его
            dict_score[name] = score + 10  # добавляем баллы команде
            # выводим данные
            print("Получены данные {} и {}".format(name, code))
            return render_template('index.html', dict_score=dict_score, form=form)
        else:
            return '<H1> Error! </H1>'
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
