from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    results = []

    if request.method == "POST":

        study_hours = float(request.form["study_hours"])

        subjects = []

        for i in range(1, 4):

            name = request.form[f"name{i}"]

            difficulty = int(request.form[f"difficulty{i}"])

            days_left = int(request.form[f"days{i}"])

            priority = (difficulty * 2) + (30 - days_left)

            subjects.append({
                "name": name,
                "difficulty": difficulty,
                "days_left": days_left,
                "priority": priority
            })

        subjects.sort(
            key=lambda x: x["priority"],
            reverse=True
        )

        total_priority = sum(
            subject["priority"]
            for subject in subjects
        )

        for subject in subjects:

            allocated_hours = (
                subject["priority"] /
                total_priority
            ) * study_hours

            results.append({
                "name": subject["name"],
                "priority": subject["priority"],
                "hours": round(
                    allocated_hours,
                    1
                )
            })

    return render_template(
        "index.html",
        results=results
    )

if __name__ == "__main__":
    app.run(debug=True)