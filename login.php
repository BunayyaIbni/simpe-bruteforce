<html>
	<head>
		<title>Form Login</title>
	</head>
	<body>
		<center>
		diberikan kata kunci: <br> <br>
		user admin password bandung katasandi telkom sukapura1 sukabirus3 sInerGiBanguNNegri kitaBisa user1 admin1 user3 admin2 akukeren1* <br> <br>
		dapatkah kamu menemukan username dan password menggunakan kata kunci diatas? <br> 
		<table width="300" align="center">
			<form method="GET" action="#">
			<tr>
				<td>Username</td>
				<td>:</td>
				<td><input name="username" type="text" id="username"/>
				</td>
			</tr>
			<tr>
				<td>Password</td>
				<td>:</td>
				<td><input name="password" type="password" id="password"/></td>
			</tr>
			<tr>
				<td><input type="submit" name="Submit" value="Login"/></td>
			</tr>
		</form>
		</table>
	</body>
</html>


<?php
if (isset($_GET['Submit'])) {
    $username = $_GET['username'];
    $password = $_GET['password'];
    
    $user = 'telkom';
    $pass = 'sInerGiBanguNNegri';
    if ($username == $user && $password == $pass) {
        echo "berhasil login";
    }
    else{
        echo "gagal login, coba lagi";
    }
    }
?>