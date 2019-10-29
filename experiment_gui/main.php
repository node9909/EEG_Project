<!-- Receive the subject number from the previous page -->
<?php
    $subname = $_POST["subname"];
?>

<html>

<head><link rel="stylesheet" type="text/css" href="main_css.css"></head>

<body onmousedown="addAnswer(event)" oncontextmenu="return false;">
    <!-- <div id="test"></div> -->
    <div class="slideshow-container" id="sl-cnt" onmousedown="return false">
        <div class="mySlides fade">
            <img src="./image/-.png" class="images">
        </div>
    </div>
    
    <!-- Slideshow script -->
    <script type="text/javascript">
        //adds 78 extra divs that will contain the images + the rectable that will block the label
        function createImages() {
            num_ims = 40;
            slide_div = document.getElementById("sl-cnt");
            for (i = 0; i<num_ims*2-1; i++) {
                slide_div.innerHTML = slide_div.innerHTML + "<div class='mySlides fade'><img src='./image/" + i.toString() + ".png' class='images'></div>"
            }
            slide_div.innerHTML = slide_div.innerHTML + '<div style="position: relative; display: table;"><div class="block" id="blocking"></div></div>'
        }
    </script>

    <script>
        var slideIndex = 0; //current slide index
        var subname = '<?php echo $subname; ?>'
        var canAnswer = false;
        var answers = new Array();
         //variable that can block mouse answers when needed
        createImages();
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

            /*document.getElementById("test").innerHTML = (answers.length).toString();
            slideIndex++;*/

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
        // calculates the milliseconds passed from the beginning to the mouse click
        // also calculates the milliseconds that passed after the reveal of the label to the mouse click
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