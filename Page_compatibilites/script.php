<?php
$data = json_decode(file_get_contents("php://input"), true);
$data1 = $data["drug1"];
$data2 = $data["drug2"];

// Escape the arguments to avoid command injection
$data1 = escapeshellarg($data1);
$data2 = escapeshellarg($data2);

// Execute the Python script with the data as arguments
$output = shell_exec("python3 process_data.py $data1 $data2");
echo $output;
?>

