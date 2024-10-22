<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['radius']) && is_numeric($_POST['radius'])) {
  $radius = floatval($_POST['radius']);
  $area = pi() * $radius * $radius;
  $circumference = 2 * pi() * $radius;

  echo "<div style='text-align: center; margin-top: 50px;'>";
  echo "<h1>Circle Results</h1>";
  echo "<p>Radius: $radius units</p>";
  echo "<p>Area: " . number_format($area, 2) . " square units</p>";
  echo "<p>Circumference: " . number_format($circumference, 2) . " units</p>";
  echo "</div>";
} else {
  echo "<div style='text-align: center; margin-top: 50px;'>";
  echo "<h1>Invalid Input</h1>";
  echo "<p>Please enter a valid numeric radius.</p>";
  echo "</div>";
}
