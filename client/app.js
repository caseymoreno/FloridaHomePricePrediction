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
    const sqft = document.getElementById("uiSqft");
    const beds = getBedValue();
    const bathrooms = getBathValue();
    const location = document.getElementById("uiLocations");
    const estPrice = document.getElementById("uiEstimatedPrice");
    console.log(`Datatype Bath ${typeof(bathrooms)}`)
    const url = "http://127.0.0.1:5000/predict_home_price"; 

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

    const url = "http://127.0.0.1:5000/get_location_names"; 
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