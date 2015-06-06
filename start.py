from flask import Flask, render_template, request, url_for

app=Flask(__name__)

@app.route('/')
def form():
	return render_template('index.html')

@app.route('/show_feeds/',methods=['POST'])
def show_feeds():
	feed_link=request.form['FLINK']
	return render_template('landing_page.html',feed_link=feed_link)

if __name__=='__main__':
	app.run(debug=True)