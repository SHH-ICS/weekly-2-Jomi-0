<!DOCTYPE html>
<html>
<head>
    <link rel="apple-touch-icon" sizes="180x180" href="favicon/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="favicon/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="favicon/favicon-16x16.png">
    <link rel="manifest" href="favicon/site.webmanifest">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">
    <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
    <title>Circle Calculator</title>
</head>
<body>
    <div class="mdl-layout mdl-js-layout mdl-layout--fixed-header">
        <header class="mdl-layout__header">
            <div class="mdl-layout__header-row">
                <span class="mdl-layout-title">Circle Calculator</span>
                <div class="mdl-layout-spacer"></div>
            </div>
        </header>
        <div class="mdl-layout__drawer">
            <span class="mdl-layout-title">Menu</span>
            <nav class="mdl-navigation">
                <a class="mdl-navigation__link" href="#">Link</a>
                <a class="mdl-navigation__link" href="#">Link</a>
                <a class="mdl-navigation__link" href="#">Link</a>
                <a class="mdl-navigation__link" href="#">Link</a>
            </nav>
        </div>
        <main class="mdl-layout__content">
            <div class="page-content" style="text-align: center; margin-top: 50px;">
                <form action="handler.php" method="POST">
                    <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
                        <input class="mdl-textfield__input" type="number" id="radius" name="radius" required>
                        <label class="mdl-textfield__label" for="radius">Enter Radius</label>
                    </div>
                    <button class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" type="submit">
                        Calculate
                    </button>
                </form>
            </div>
        </main>
    </div>
</body>
</html>
