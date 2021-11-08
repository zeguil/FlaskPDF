import pdfkit 
from flask import Flask, render_template, make_response
app = Flask(__name__)

@app.route("/pdf")
def gerar_pdf():
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    rendered = render_template("hello.html")
    pdf = pdfkit.from_string(rendered, False, configuration=config)
    
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
    return response
    
    
if __name__ == "__main__":
    app.run(debug=True)
