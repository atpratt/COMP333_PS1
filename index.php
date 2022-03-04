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
	//Make sure this dbname is the same as the db name in your

    // Create server connection.
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Check server connection.
    #Trying to connect to server
    if ($conn->connect_error) {
      // Exit with the error message.
        die("Connection failed: " . $conn->connect_error);
    }

    $out_value = "";

    #Registration
    if(isset($_REQUEST["Registration"])){
      // Variables for the output and the web form below.
        $out_reg = "";
        $username = $_REQUEST['Username'];
        $password = $_REQUEST['Password'];

      // Check that the user entered data in the form.
        if(!empty($username) && !empty($password)){
            $sql_query = "SELECT * FROM users WHERE Username = ('$username')";
            $result = mysqli_query($conn, $sql_query);
            $userrow = mysqli_fetch_assoc($result);
            #if username already in db
            if (mysqli_num_rows($result) > 0) {
                $out_reg = "The username " . $username . " has already been taken.  Please choose a different username.";
            }
            #if new username
            else {
                $sql_query = "INSERT INTO users (username, password) VALUES ('$username', '$password')";
                $result = mysqli_query($conn, $sql_query);
                if (mysqli_num_rows($result) > 0){
                    $out_reg = "Successfully registered user " . $username;
                }
                else {
                    $out_reg = "An error has occurred and " . $username . " has not been regoistered.";
                }
            }
        }
        else {
            $out_reg = "You'll need to enter a username and password!";
        }
    }

    #Song Retrieval
    if(isset($_REQUEST["Song_Retrieval"])) {
        $out_song = "";
        $username = $_REQUEST["Rater"];

        #if some usernamne entered
        if(!empty($username)){
            #Check usernamne in db, query users table
            $sql_query = "SELECT * FROM users WHERE username = ('$username')";
            $result = mysqli_query($conn, $sql_query);
            #if usernname in db
            if (mysqli_num_rows($result) > 0) {
                #query ratings table
                $sql_query = "SELECT * FROM ratings WHERE username = ('$username')";
                #$sql_query_artist = "SELECT * FROM a WHERE username = ('$username')";
                $result = mysqli_query($conn, $sql_query);
                #check if there are any ratings for that username
                if (mysqli_num_rows($result) > 0) {
                    #print each song and its rating
                    while($ratings = mysqli_fetch_assoc($result)) {
                        $out_song = $out_song . $username . " has rated '" . $ratings["song"] . "' a " . $ratings["rating"] . "." . "<br>";
                    }
                }
                #if no ratings for that username
                else {
                    $out_song = "The user " . $username . " has no ratings yet.";
                }
            }
            #if username not in db
            else {
                $out_song = "Username " . $username . " has not yet been registered.";
            }
        }
        #if no username entered
        else {
            $out_song = "First you'll need to enter a username.";
        }
    }
    $conn->close();
  ?>

<!--HTML -->
  <div class="forms">

  <h1> Registration </h1>
  <form method="GET" action="">
  Username: <input type="text" name="Username" placeholder="New Username" /><br>
  Password: <input type="text" name="Password" placeholder="New Password" /><br>
  <input type="submit" name="submit" value="Submit"/>
  <p>
  <?php
  if(!empty($out_reg)){
      echo $out_reg;
  }
  ?>
  <p>
  </form>

  <h1> Song Retrieval </h1>
  <form method="GET" action="">
  Username: <input type="text" name="Rater" placeholder="Rater's Username" /><br>
  <input type="submit" name="Song_Retrieval" value="Retrieve"/>
  <p>
  <?php
  if(!empty($out_song)){
      echo $out_song;
  }
  ?>
  <p>
  </form>
  </div>

</body>
</html>
