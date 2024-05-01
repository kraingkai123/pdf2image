<?php
// Data to be sent
$data = array(
    'pdf_file' => '1.pdf',
    'output_folder' => 'output_images/'
);

// Encode data as JSON
$data_json = json_encode($data);

// URL of the Python script
$python_script_url = 'http://127.0.0.1:5000/convertpdf2image';

/* $data = array(
    'key1' => 'value1',
    'key2' => 'value2'
); */

$ch = curl_init($python_script_url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
curl_close($ch);

echo $response; // แสดงข้อมูลที่ถูกประมวลผลจาก Python
?>