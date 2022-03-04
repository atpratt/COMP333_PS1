<!--Write an index.php script using HTML, SQL, PHP that retrieves data from the music-db database
that you have created under 1(b) via a graphical user interface using HTML forms.

Features to Include
It should allow a new user to register with a username and password.
The submitted username and password should be written to the users table of your music-db database.
If a user enters a username that is already taken, the user should be alerted to pick a different username. (Passwords do not need to be unique)
Upon entering a username, all songs that the user has rated, including the user’s rating should be returned. Songs that the user did not rate should not be returned.
You do not need to populate the database with songs through an HTML form; you can assume it is already populated
-->

<!DOCTYPE HTML>
<html lang="en">
<head>

<meta http-equiv="Content-Type" content="application/x-www-form-urlencoded"/>

<title>COMP333 HW2</title>
<link rel="stylesheet" href="stylesheet.css">
</head>

<body>
  <?php
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "music-db";
	

    // Create server connection.
    $conn = new mysqli($servername, $username, $password, $dbname);

    #Trying to connect to server
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $out_value = "";

    #Registration
    if(isset($_REQUEST["Registration"])) {
    
        #$out_reg = "";
        $reg_username = $_REQUEST['Username'];
        $reg_password = $_REQUEST['Password'];

      // Check that the user entered data in the form.
        if(!empty($reg_username) && !empty($reg_password)) {
            $sql_query = "SELECT * FROM users WHERE username = ('$reg_username')";
            $result = mysqli_query($conn, $sql_query);
            #$userrow = mysqli_fetch_assoc($result);
            #if username already in db
            if (mysqli_num_rows($result) > 0) {
                $out_value = "The username '" . $reg_username . "' has already been taken.  Please choose a different username.";
            }
            #if new username
            else {
                #insert username, password into db
                $sql_query = "INSERT INTO users (username, password) VALUES ('$reg_username', '$reg_password')";
                $result = mysqli_query($conn, $sql_query);
                #check that new username added to db
                $sql_query = "SELECT * FROM users WHERE username = ('$reg_username')";
                $result = mysqli_query($conn, $sql_query);
                #if in db
                if (mysqli_num_rows($result) > 0) {
                    $out_value = "Successfully registered user '" . $reg_username . "'";
                }
                #if not in db
                else {
                    $out_value = "An error has occurred and '" . $reg_username . "' has not been registered.";
                }
            }
        }
        else {
            $out_value = "You'll need to enter both a username and password!";
        }
    }

    #Song Retrieval
    if(isset($_REQUEST["Song_Retrieval"])) {
        #$out_song = "";
        $retr_username = $_REQUEST["Rater"];

        #if some usernamne entered
        if(!empty($retr_username)) {
            #Check usernamne in db, query users table
            $sql_query = "SELECT * FROM users WHERE username = ('$retr_username')";
            $result = mysqli_query($conn, $sql_query);
            #if usernname in db
            if (mysqli_num_rows($result) > 0) {
                #query ratings table
                $sql_query = "SELECT * FROM ratings WHERE username = ('$retr_username')";
                #$sql_query_artist = "SELECT * FROM a WHERE username = ('$username')";
                $result = mysqli_query($conn, $sql_query);
                #check if there are any ratings for that username
                if (mysqli_num_rows($result) > 0) {
                    #print each song and its rating
                    while($ratings = mysqli_fetch_assoc($result)) {
                        $out_value = $out_value . "User '" . $retr_username . "' has given the song '" . $ratings["song"] . "' a rating of " . $ratings["rating"] . "." . "<br>";
                    }
                }
                #if no ratings for that username
                else {
                    $out_value = "The user '" . $retr_username . "' has no ratings yet.";
                }
            }
            #if username not in db
            else {
                $out_value = "Username '" . $retr_username . "' has not yet been registered.";
            }
        }
        #if no username entered
        else {
            $out_value = "First you'll need to enter a username.";
        }
    }
    $conn->close();
  ?>

<!--HTML -->
  <div class="forms">

  <h1> Registration </h1>
  <form method="GET" action="">
  Username: <input type="text" name="Username" placeholder="New Username" /><br>
  Password: <input type="password" name="Password" placeholder="New Password" /><br>
  <input type="submit" name="Registration" value="Submit"/>
  <p>
  <?php
  #if(!empty($out_value)){
  #    echo $out_value;
  #}
  ?>
  <p>
  </form>


  <h1> Song Retrieval </h1>
  <form method="GET" action="">
  Username: <input type="text" name="Rater" placeholder="Rater's Username" /><br>
  <input type="submit" name="Song_Retrieval" value="Retrieve"/>
  <p>
  
  </form>
  <div>
  <?php
  if(!empty($out_value)) {
      echo $out_value;
  }
  ?>
  <p>
  </div>

</body>
</html>
