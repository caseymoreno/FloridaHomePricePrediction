function getBathValue() {
    let uiBathrooms = document.getElementById("bath-select-menu").value;
    console.log(parseInt(uiBathrooms))
    return parseInt(uiBathrooms);
  }
  
  function getBedValue() {
    let uiBeds = document.getElementById("bed-select-menu").value;
    console.log(parseInt(uiBeds))
    return parseInt(uiBeds);
  }
  
  function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft");
    var beds = getBedValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");
    console.log(`Datatype Bath ${typeof(bathrooms)}`)
    var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
    $.post(url, {
        sq_feet: parseFloat(sqft.value),
        location: location.value,
        beds: beds,
        baths: bathrooms
    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " USD";
        console.log(status);
    });
    console.log(`Baths: ${bathrooms}`)
  }
  
  function onPageLoad() {
    console.log( "document loaded" );

    var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
  }
  
  window.onload = onPageLoad;

  console.log("Sdf");