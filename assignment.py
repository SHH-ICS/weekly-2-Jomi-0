<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">
    <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Circle Calculator</title>
</head>
<body>
    <div class="mdl-layout mdl-js-layout mdl-layout--fixed-header">
        <header class="mdl-layout__header">
            <div class="mdl-layout__header-row">
                <span class="mdl-layout-title">Circle Calculator</span>
            </div>
        </header>
        <main class="mdl-layout__content">
            <div class="page-content" style="text-align: center; margin-top: 50px;">
                <form method="POST" action="handler.php">
                    <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
                        <input class="mdl-textfield__input" type="text" id="radius" name="radius" required>
                        <label class="mdl-textfield__label" for="radius">Enter Radius</label>
                    </div>
                    <button class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored" type="submit">
                        Calculate
                    </button>
                </form>
            </div>
        </main>
    </div>
</body>
</html>

