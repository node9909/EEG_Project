<!-- Receive the subject number from the previous page -->
<?php
    $subname = $_POST["subname"];
?>

<html>

<style type="text/css">
    * {box-sizing:border-box}
    
    /*Sudo class for disabling highlighting*/
    ::selection {
        background-color: transparent;
        color: #000;
    }

    .slideshow-container {
        max-width: 1000px;
        position: relative;
        left: 62%;
        top: 20%;
        transform: translateX(-50%);
        margin: auto;
    }

    /* Hide the images by default */
    .mySlides::selection{
        display: none;
    }

    /* Fading animation */
    .fade {
        -webkit-animation-name: fade;
        -webkit-animation-duration: 1.5s;
        animation-name: fade;
        animation-duration: 1.5s;
    }

    .block {
        display: none;
        background-color: white;
        position: absolute;
        border: 2px solid black;
        padding: 20px 150px;
        top: 82%;
        left: 5%
    }

    @-webkit-keyframes fade {
        from {opacity: .4}
        to {opacity: 1}
    }

    @keyframes fade {
        from {opacity: .4}
        to {opacity: 1}
    }
</style>

<body onmousedown="addAnswer(event)" oncontextmenu="return false;">
    
    <div class="slideshow-container" onmousedown="return false">
        <div class="mySlides fade">
            <img src="./image/-.png" style="width:40%">
        </div>

        <div class="mySlides fade">
            <img src="./image/0.png" style="width:40%">
        </div>

        <div class="mySlides fade">
            <img src="./image/1.png" style="width:40%">
        </div>

        <div class="mySlides fade">
            <img src="./image/2.png" style="width:40%">
        </div>

        <div class="mySlides fade">
            <img src="./image/3.png" style="width:40%">
        </div>

        <div class="mySlides fade">
            <img src="./image/4.png" style="width:40%">
        </div>

        <div class="mySlides fade">
            <img src="./image/5.png" style="width:40%">
        </div>

        <div class="mySlides fade">
            <img src="./image/6.png" style="width:40%">
        </div>

        <div class="mySlides fade">
            <img src="./image/7.png" style="width:40%">
        </div>
        
        <div class="mySlides fade">
            <img src="./image/8.png" style="width:40%">
        </div>
        <!-- Blocking the label for x secs -->
        <div class="block" id="blocking"></div>

    </div>

    <!-- Slideshow script -->
    <script>
        var slideIndex = 0; //current slide index
        var subname = '<?php echo $subname; ?>'
        var canAnswer = false; //variable that can block mouse answers when needed
        showSlides();

        function showSlides() {
            var i;
            var slides = document.getElementsByClassName("mySlides");
            for (i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";
            }
            slideIndex++;
            if (slideIndex > slides.length) {
                download(subname + '.txt'); // when slideshow ends save file
                document.location.href = "./end.html" // and change url
            } 
            slides[slideIndex-1].style.display = "block";
            if (slideIndex % 2 == 0 ){ //Slides with odd index are baseline crosses
                canAnswer = true;
                document.getElementById("blocking").style.display = "block";
                setTimeout(function() {
                    document.getElementById("blocking").style.display = "none"
                }, 5000);
                setTimeout(showSlides, 10000);
            } else {
                canAnswer = false;
                document.getElementById("blocking").style.display = "none";
                setTimeout(showSlides, 5000);
            }
        }

    </script>


    <script>
        var answers = new Array(); 
        var times = new Array();
        var startTime = Date.now();
        // Appends new answer to the answers variable if canAnswer flag is true
        // Also calculates the milliseconds passed from the beginning to the mouse click
        function addAnswer(event) {
            if (canAnswer) {
                answers.push(event.button);
                document.getElementById("kwlos").innerHTML = answers;
            } 

            times.push(Date.now()-startTime);
            canAnswer = false;
        }

        // Downloads the final file
        function download(filename) {
            var pom = document.createElement('a');
            pom.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(answers.toString() + '\n' + times.toString()));
            pom.setAttribute('download', filename);

            if (document.createEvent) {
                var event = document.createEvent('MouseEvents');
                event.initEvent('click', true, true);
                pom.dispatchEvent(event);
            }
            else {
                pom.click();
            }
        }

    </script>

</body>
</html>