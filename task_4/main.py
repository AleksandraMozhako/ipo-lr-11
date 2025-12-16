import json

def generate_html():
    with open("data.json", "r", encoding="utf-8") as f:
        quotes_data = json.load(f)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Quotes Collection</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f3cb97f1;
                margin: 0;
                padding: 20px;
            }}
            h1 {{
                text-align: center;
                color: #9e4141;
            }}
            table {{
                width: 80%;
                margin: 20px auto;
                border-collapse: collapse;
            }}
            th, td {{
                padding: 12px;
                text-align: left;
                border-bottom: 1px solid #9e4141;
            }}
            th {{
                background-color: #9e4141;
                color: white;
            }}
            a {{
                display: block;
                text-align: center;
                margin-top: 20px;
                color: #9e4141;
            }}
        </style>
    </head>
    <body>
        <h1>Quotes Collection</h1>
        <table>
            <thead>
                <tr>
                    <th>Quote</th>
                    <th>Author</th>
                </tr>
            </thead>
            <tbody>
    """

    for quote in quotes_data:
        html_content += f"""
                <tr>
                    <td>{quote['quote']}</td>
                    <td>{quote['author']}</td>
                </tr>
        """

    html_content += f"""
            </tbody>
        </table>
        <a href="https://quotes.toscrape.com/" target="_blank">Источник данных</a>
    </body>
    </html>
    """

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("HTML-файл успешно сгенерирован: index.html")

if __name__ == "__main__":
    generate_html()