let firstStep = 1
let currentStep = 1
let lastStep = 3
var velikostPorcije = 0;
let kosmic1 = 0
let kosmic2 = 0
let kosmic3 = 0
let obratMotorja = 0.1
var vrednost1 = 0
var vrednost2 = 0
var vrednost3 = 0

var handlesSlider4 = document.getElementById("slider-handles4");

noUiSlider.create(handlesSlider4, {
    start: [33, 67],
    connect: [true, true, true],
  step: 1,
    range: {
        'min': [0],
        'max': [100]
    }
});
    // # za id, . za class
    $(document).ready(function(){
      $("#currentPage").text(currentStep)
      $("#lastPage").text(lastStep)
      $("#1.screen").show();
      if (velikostPorcije == 0){
        $(".next-step").addClass("disabled")
      }
    })
    // Screen 1
    $(".size").click(function(){
      $(".size").each(function() {
        $(this).removeClass("selected-size");
      })
      velikostPorcije = parseInt($(this).attr('id'));
      $("#" + velikostPorcije).addClass("selected-size");
      console.log("velikost porcije" + velikostPorcije);
      if (velikostPorcije != 0){
        $(".next-step").removeClass("disabled")
      }
    })

  // Screen 2
  handlesSlider4.noUiSlider.on('update', function (values, handle, unencoded) {
    var razmerje = values;
    //onsole.log(razmerje)
    kosmic1 = (razmerje[0]) - 0; 
    // lahko da se podatkovni tipi kej ne ujemaj
    // lahko da je nekje string ubistvu
    // za dobit int iz stringa: parseInt(a);
    kosmic2 = (razmerje[1]) - (razmerje[0]);
    kosmic3 = 100 - (kosmic1) - (kosmic2);
    //console.log(kosmic1);
    //console.log(kosmic2);
    //console.log(kosmic3);

    $("#kosmic1").text(kosmic1);
    $("#kosmic2").text(kosmic2);
    $("#kosmic3").text(kosmic3);
    
    vrednost1 =  parseInt(kosmic1) / 100 *  parseInt(velikostPorcije);
    vrednost2 =  parseInt(kosmic2) / 100 *  parseInt(velikostPorcije);
    vrednost3 =  parseInt(kosmic3) / 100 *  parseInt(velikostPorcije);
    //console.log(Math.round(vrednost1 * 10) / 10 + " obratov");
    //console.log(Math.round(vrednost2 * 10) / 10 + " obratov");
    //console.log(Math.round(vrednost3 * 10) / 10 + " obratov");
    // mala: 1, srednja: 2, velika: 3
    // 1 obrat motorja = 0.1
    // razmerje: 0.25, 0.50, 0.25 -> mala porcija: 0.25, 0.5, 0.25, srednja porcija: 0.5, 1. 0.5 ..

    // imamo podatek za obrate motorja: prvi motor: 0.5 = 5x, drugi motor: 1 = 10x, tretji motor = 0.5 = 5x
    // api endpoint na katerega bomo poslali te vrednosti
    
      

    // vrednosti iz teh spremenljivk se morajo še izpisati nekam na zaslon
      // obrati2
});
// tole sporžimo ko se klikne na en gumb
  $("#zacni").click(function() {
    console.log("zacni")
    $.get( "/motor/0/" + String(vrednost1), function( data ) {
        //console.log("data")
        
      }).done(function() {
          $.get( "/motor/1/" + String(vrednost2), function( data ) {
      }).done(function() {
          $.get( "/motor/2/" + String(vrednost3), function( data ) {
        
      }).done(function() {
          alert( "konec 3" );
        });
        });
        });
    
    
  })

    $(".next-step").click(function(){
      currentStep = currentStep + 1
      $("#" + (currentStep - 1) + ".screen").hide();
      $("#" + currentStep + ".screen").show();
      if (currentStep == lastStep) {
        $(".next-step").hide();
      } 
      
    if (currentStep > firstStep) {
        $(".previous-step").show();
      } //potem next-step na hide
      
    })
if (currentStep == firstStep) {
          $(".previous-step").hide();
        }
 
  $(".previous-step").click(function(){
        //console.log(currentStep)
        currentStep = currentStep - 1
        //console.log(currentStep)
        $("#" + currentStep + ".screen").show();
        $("#" + (currentStep + 1) + ".screen").hide(); 
        if (currentStep == firstStep) {
          $(".previous-step").hide();
        }
    if (currentStep < lastStep) {
        $(".next-step").show();
      }
      //if currentstep == firstStep potem next-step na hide
    // dodaj še da se prikaže gumb za naprej, če smo šli iz zadnjega screena enega nazaj
      })

