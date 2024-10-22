<!DOCTYPE html>
<html>

<head>
  <title>Circle Calculator</title>
  <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">
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