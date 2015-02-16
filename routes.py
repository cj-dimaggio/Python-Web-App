from flask import Blueprint, render_template, request, redirect, url_for
import db

routes = Blueprint('routes', __name__)

@routes.route('/admin/tokens', methods=['POST', 'GET'])
def tokens():
    if request.method == 'POST':
        name = request.form['token']
        db.createToken(name)
        return render_template('tokens.html', tokens=db.readTokens())
    elif request.method == 'DELETE':
        tokenIds = request.form.getlist('tokenId')
    return render_template('tokens.html', tokens=db.readTokens())

# I would have much rathered keep this RESTful and just add a DELETE method check
# within /tokens route but currently most browsers only support forms submitting POST
# and GET. We could have theoretically used ajax to send the DELETE request but this
# just simplifies things for prototyping purposes
@routes.route('/admin/tokens/delete', methods=['POST'])
def deleteTokesn():
    tokenIds = request.form.getlist('tokenId')
    db.deleteTokens(tokenIds)
    return redirect(url_for('.tokens'))

@routes.route('/admin/questions', methods=['POST', 'GET'])
def questions():
    return render_template('questions.html', questions=db.readQuestions())

@routes.route('/admin/questions/<questionId>', methods=['POST', 'GET'])
def question(questionId):
    return render_template('question-single.html', question=db.getQuestion(questionId))
