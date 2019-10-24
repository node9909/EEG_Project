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
        width: 100%;
        height: auto;
        max-width: 1000px;
        left: 50%;
        top: 10%;
        /*border: 2px solid black;*/
        transform: translateX(-50%, -50%);
        margin: auto;
        overflow: hidden;
    }

    /* Hide the images by default */
    .mySlides::selection{
        display: none;
    }

    .images {
        max-width: 500px;
        max-height: auto;
        left: 50%;
        position: relative;
        transform: translate(-50%);
    }
    /* Fading animation */
    .fade {
        -webkit-animation-name: fade;
        -webkit-animation-duration: 1.5s;
        animation-name: fade;
        animation-duration: 1.5s;
    }

    .block {
        /*width: 100%;*/
        background-color: white;
        /*border: 2px solid black;*/
        display: none;        
        position: absolute;
        height: 120px;
        width: 800px;
        bottom: -40%;
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
    <!-- <div id="test"></div> -->
    <div id="kwlos"></div>
    <div class="slideshow-container" onmousedown="return false">
        <div class="mySlides fade">
            <img src="./image/-.png" class="images">
        </div>

        <div class="mySlides fade">
            <img src="./image/0.png" class="images">
        </div>

        <div class="mySlides fade">
            <img src="./image/1.png" class="images">
        </div>

        <div class="mySlides fade">
            <img src="./image/2.png" class="images">
        </div>

        <div class="mySlides fade">
            <img src="./image/3.png" class="images">
        </div>

        <div class="mySlides fade">
            <img src="./image/4.png" class="images">
        </div>

        <div class="mySlides fade">
            <img src="./image/5.png" class="images">
        </div>

        <div class="mySlides fade">
            <img src="./image/6.png" class="images">
        </div>

        <div class="mySlides fade">
            <img src="./image/7.png" class="images">
        </div>
        
        <div class="mySlides fade">
            <img src="./image/8.png" class="images">
        </div>
        <!-- Blocking the label for x secs -->
        <div style="position: relative; display: table;"><div class="block" id="blocking"></div></div>

    </div>
    
    <!-- Slideshow script -->
    <script>
        var slideIndex = 0; //current slide index
        var subname = '<?php echo $subname; ?>'
        var canAnswer = false;
        var answers = new Array();
         //variable that can block mouse answers when needed
        showSlides();

        function showSlides() {
            var i;
            var slides = document.getElementsByClassName("mySlides");
            for (i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";
            }
            if (Math.floor(slideIndex/2) != answers.length) { 
                answers.push(1);
                times.push(0);
                ans_times.push(0);
            }
            document.getElementById("kwlos").innerHTML = (answers.length).toString();
            slideIndex++;
            

            if (slideIndex > slides.length) {
                download(subname + '.txt'); // when slideshow ends save file
                document.location.href = "./end.html" // and change url
            } 
            slides[slideIndex-1].style.display = "block";
            if (slideIndex % 2 == 0 ){ //Slides with odd index are baseline crosses
                
                document.getElementById("blocking").style.display = "block";
                setTimeout(function() {
                    document.getElementById("blocking").style.display = "none";
                    canAnswer = true;
                    label_time = Date.now();
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
        var times = new Array();
        var ans_times = new Array();
        var startTime = Date.now();
        // Appends new answer to the answers variable if canAnswer flag is true
        // Also calculates the milliseconds passed from the beginning to the mouse click
        function addAnswer(event) {
            if (canAnswer) {
                answers.push(event.button);
                ans_times.push(Date.now() - label_time)
                times.push(Date.now()-startTime);
            } 
            canAnswer = false;
        }

        // Downloads the final file
        function download(filename) {
            var pom = document.createElement('a');
            pom.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(answers.toString() + '\n' + times.toString() + '\n' + ans_times.toString()));
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