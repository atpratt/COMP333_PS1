Write an index.php script using HTML, SQL, PHP that retrieves data from the music-db database 
that you have created under 1(b) via a graphical user interface using HTML forms. 

Features to Include
It should allow a new user to register with a username and password. 
The submitted username and password should be written to the users table of your music-db database. 
If a user enters a username that is already taken, the user should be alerted to pick a different username. (Passwords do not need to be unique)
Upon entering a username, all songs that the user has rated, including the user’s rating should be returned. Songs that the user did not rate should not be returned.
You do not need to populate the database with songs through an HTML form; you can assume it is already populated


<!DOCTYPE HTML>
<html lang="en">
<head>

  <meta http-equiv="Content-Type" content="application/x-www-form-urlencoded"/>
<title>COMP333_PS2</title>
</head>

<body>
  <!-- 
    PHP code for retrieving data from the database.
  -->
  <?php
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "music-db";
	//Make sure this dbname is the same as the db name in your 

    // Create server connection.
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Check server connection.
    if ($conn->connect_error) {
      // Exit with the error message.
      // . is used to concatenate strings.
      die("Connection failed: " . $conn->connect_error);
    }

    // `isset` — Function to determine if a variable is declared and is different than null.
    // $_REQUEST is a PHP super global variable which is used to collect data after submitting an HTML form.
    if(isset($_REQUEST["submit"])){
      // Variables for the output and the web form below.
      $out_value = "";
      $username = $_REQUEST['Username'];
      $password = $_REQUEST['Password'];

      // The following is the core part of this script where we connect PHP
      // and SQL.
      // Check that the user entered data in the form.
      if(!empty($username) && !empty($password)){
        // If so, prepare SQL query with the data.
        $sql_query = "SELECT * FROM Username WHERE Password = ('$username') AND test = ('$password')";
        // Send the query and obtain the result.
        // mysqli_query performs a query against the database.
        $result = mysqli_query($conn, $sql_query);
        // mysqli_fetch_assoc returns an associative array that corresponds to the 
        // fetched row or NULL if there are no more rows.
        // Probably does not make much of a difference here, but, e.g., if there are
        // multiple rows returned, you can iterate over those with a loop.

		//for each over result

        $row = mysqli_fetch_assoc($result);
		//return array/list and we should be able to itterate over to get songs
        $out_value = "Songs Reviewed By User " . $row['song'] . $row['rating'];
      }
      else {
        $out_value = "No raitings available!";
      }
    }

    $conn->close();
  ?>

  <!-- 
    HTML code for the form by which the user can query data.
    Note that we are using names (to pass values around in PHP) and not ids
    (which are for CSS styling or JavaScript functionality).
    You can leave the action in the form open 
    (https://stackoverflow.com/questions/1131781/is-it-a-good-practice-to-use-an-empty-url-for-a-html-forms-action-attribute-a)
  -->
  <form method="GET" action="">
  Username: <input type="text" name="Username" placeholder="Enter Username" /><br>
  Password: <input type="text" name="Password" placeholder="Enter Password" /><br>
  <input type="submit" name="submit" value="Submit"/>
  <!-- 
    Make sure that there is a value available for $out_value.
    If so, print to the screen.
  -->
  <p><?php 
    if(!empty($out_value)){
      echo $out_value;
    }
  ?></p>
  </form>


</body>
</html>

