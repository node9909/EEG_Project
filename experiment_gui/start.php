<html>

<style type="text/css">
	
	.form-container {
		position: absolute;
		left: 50%;
		top: 50%;
		transform: translate(-50%, -50%);
	}

	.submit-but {
		position: relative;
		left: 50%;
		transform: translate(-50%);
		margin-top: 20px;
		padding: 16px 32px;
	}


</style>


<body>
	<div class="form-container">
		<form action="./main.php" method="post">
			<input type="text" name="subname" style="text-align: center"></br>
			<input type="submit" value="Start" class="submit-but">
		</form>
	</div>

</body>

</html>