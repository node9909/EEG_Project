<?php
    $subname = $_POST["subname"];
?>

<html>

<style type="text/css">
    * {box-sizing:border-box}
    
    .slideshow-container {
        max-width: 1000px;
        position: relative;
        left: 62%;
        top: 20%;
        transform: translateX(-50%);
        margin: auto;
    }

    /* Hide the images by default */
    .mySlides {
        display: none;
    }

    /* Fading animation */
    .fade {
        -webkit-animation-name: fade;
        -webkit-animation-duration: 1.5s;
        animation-name: fade;
        animation-duration: 1.5s;
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

    <div class="slideshow-container">
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


    </div>

    <script>
        var slideIndex = 0;
        var subname = '<?php echo $subname; ?>'
        showSlides();

        function showSlides() {
            var i;
            var slides = document.getElementsByClassName("mySlides");
            for (i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";
            }
            slideIndex++;
            if (slideIndex > slides.length) {download(subname + '.txt'); document.location.href = "./end.html"}
            slides[slideIndex-1].style.display = "block";
            if (slideIndex % 2 == 0 ){
                document.onkeypress = function(e) {
                    e = e || window.event;
                }
                setTimeout(showSlides, 10000);
            } else {
                setTimeout(showSlides, 5000);
            }
        }

    </script>

    <script>
        var answers = new Array(); 
        var times = new Array();
        var startTime = Date.now();
        function addAnswer(event) {
            answers.push(event.button);
            times.push(Date.now()-startTime);
        }

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