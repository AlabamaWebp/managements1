import os

for fileindex in range(1,16):
    with open(f"{fileindex}.html", "w", encoding="utf-8") as file:
        file.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="style.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div class="content">

    </div>
    <div class="footer">
        <a href="index.html">Назад</a>
    </div>
</body>
</html>""")