from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import jinja2


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "secretSECRETseekrit"

JOB_LIST = ["Software Engineer", "QA Engineer", "Product Manager"]

# YOUR ROUTES GO HERE
@app.route("/")
def index():
    """Return homepage."""

    return render_template("index.html")

@app.route("/application-form")
def app_form():
	"""Return application form."""

	return render_template("application-form.html",
							JOB_LIST=JOB_LIST)

@app.route("/application-success", methods=["POST"])
def app_form_response():
	"""Displays individualized confirmation response to application form submittal."""

	first_name = request.form.get("first-name")
	last_name = request.form.get("last-name")
	salary = int(request.form.get("salary"))
	position  = request.form.get("position")

	for job in JOB_LIST:
		if position in job:
			position = job

	return render_template("application-response.html",
							first_name=first_name,
							last_name=last_name,
							salary=salary,
							position=position)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
