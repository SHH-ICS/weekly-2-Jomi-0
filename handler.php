<!DOCTYPE html>
<html>

  <head>
    <title>Circle Calculator</title>
    <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">
    <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <!-- Always shows a header, even in smaller screens. -->
    <div class="mdl-layout mdl-js-layout mdl-layout--fixed-header">
      <header class="mdl-layout__header">
        <div class="mdl-layout__header-row">
          <!-- Title -->
          <span class="mdl-layout-title">Title</span>
          <!-- Add spacer, to align navigation to the right -->
          <div class="mdl-layout-spacer"></div>
          <!-- Navigation. We hide it in small screens. -->
          <nav class="mdl-navigation mdl-layout--large-screen-only">
            <a class="mdl-navigation__link" href="">Link</a>
            <a class="mdl-navigation__link" href="">Link</a>
            <a class="mdl-navigation__link" href="">Link</a>
            <a class="mdl-navigation__link" href="">Link</a>
          </nav>
        </div>
      </header>
      <div class="mdl-layout__drawer">
        <span class="mdl-layout-title">Title</span>
        <nav class="mdl-navigation">
          <a class="mdl-navigation__link" href="">Link</a>
          <a class="mdl-navigation__link" href="">Link</a>
          <a class="mdl-navigation__link" href="">Link</a>
          <a class="mdl-navigation__link" href="">Link</a>
        </nav>
      </div>
      <main class="mdl-layout__content">
        <div class="page-content"><!-- Your content goes here --></div>
      </main>
    </div>
  </head>

  <body>
    <?php
    if (isset($_POST['radius']) && is_numeric($_POST['radius'])) {
      $radius = floatval($_POST['radius']);
      $area = pi() * $radius * $radius;
      $circumference = 2 * pi() * $radius;

      echo "<h1>Circle Calculator</h1>";
      echo "<p>Radius: $radius units</p>";
      echo "<p>Area: " . number_format($area, 2) . " square units</p>";
      echo "<p>Circumference: " . number_format($circumference, 2) . " units</p>";
    } else {
      echo "<h1>Invalid Input</h1>";
      echo "<p>Please enter a valid numeric radius.</p>";
    }
    ?>
  </body>

</html>