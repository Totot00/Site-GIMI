<?php

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Préparation des données pour les envoyer au script Python
    $patientName = escapeshellarg($_POST['patientName']);
    $room = escapeshellarg($_POST['room']);
    $medication = escapeshellarg($_POST['medication']);
    $flowRate = escapeshellarg($_POST['flowRate']);
    $volume = escapeshellarg($_POST['volume']);

    // Appel du script Python avec les données
    $output = shell_exec("python3 processInjection.py $patientName $room $medication $flowRate $volume");

    // Vous pouvez traiter ou afficher $output si nécessaire
    echo "<div class='alert'>Résultat : $output</div>";
}

?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Ajout d'Injection</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f6f9;
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 600px;
            margin: 50px auto;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 40px 30px;
        }

        h1 {
            color: #007BFF;
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
        }

        input[type="text"] {
            width: 100%;
            padding: 8px 12px;
            margin-bottom: 15px;
            border: 1px solid #e0e0e0;
            border-radius: 4px;
            font-size: 16px;
        }

        input[type="submit"] {
            background-color: #007BFF;
            color: #ffffff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        input[type="submit"]:hover {
            background-color: #0056b3;
        }

        .alert {
            border: 1px solid #FFC107;
            padding: 10px;
            margin-top: 20px;
            background-color: #FFF8E1;
            color: #856404;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Ajout d'Injection</h1>
        <form action="" method="POST">
            <div>
                <label for="patientName">Nom du patient :</label>
                <input type="text" id="patientName" name="patientName" required>
            </div>
            <div>
                <label for="room">Chambre :</label>
                <input type="text" id="room" name="room" required>
            </div>
            <div>
                <label for="medication">Médicament :</label>
                <input type="text" id="medication" name="medication" required>
            </div>
            <div>
                <label for="flowRate">Débit :</label>
                <input type="text" id="flowRate" name="flowRate" required>
            </div>
            <div>
                <label for="volume">Volume :</label>
                <input type="text" id="volume" name="volume" required>
            </div>
            <div>
                <input type="submit" value="Ajouter">
            </div>
        </form>
    </div>
</body>
</html>
