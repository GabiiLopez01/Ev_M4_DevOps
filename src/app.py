from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>HealthTrack</title>
        </head>
        <body>
            <h1>HealthTrack</h1>
            <div id="registro">
                <input type="text" id="nombre" placeholder="Nombre">
                <input type="number" id="peso" placeholder="Peso (kg)">
                <button id="btn-registrar">Registrar</button>
            </div>
            <div id="peso-actual" style="margin-top: 20px;"></div>
            
            <script>
                document.getElementById("btn-registrar").addEventListener("click", function() {
                    const nombre = document.getElementById("nombre").value;
                    const peso = document.getElementById("peso").value;
                    document.getElementById("peso-actual").textContent = "Peso actual: " + peso + " kg";
                });
            </script>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)