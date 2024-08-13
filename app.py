from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/firewall', methods=['GET', 'POST'])
def firewall():
    #Fetch existing firewall rules
    results = subprocess.run(['sudo', 'iptables', '-S'], capture_output=True, text=True)
    rules = results.stdout.splitlines()

    return render_template('firewall.html', rules=rules)

@app.route('/firewall/add', methods=['POST'])
def add_rule():
    rule = request.form['rule']
    # Add the rule using iptables
    subprocess.run(['sudo'] + rule.split(), check=True)
    return redirect(url_for('firewall'))

@app.route('/firewall/delete', methods=['POST'])
def delete_rule():
    rule = request.form['rule']
    # Delete the rule using iptables
    rule_parts = rule.split()
    delete_rule = ['sudo', 'iptables', '-D'] + rule_parts[1:]  # Convert to delete command
    subprocess.run(delete_rule, check=True)
    return redirect(url_for('firewall'))

@app.route('/ids')
def ids():
    return render_template('ids.html')

@app.route('/backup')
def backup():
    return render_template('backup.html')

if __name__ == '__main__':
    app.run(debug=True)