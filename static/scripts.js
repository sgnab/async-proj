$(document).ready(function(){

    var cars = {
        "Honda": ['Civic', 'Accord', 'CR-V'],
        "Ford":["Focus","Taurus","Escape"],
        "Volkswagen":["Jetta","Passat","Tiguan"]
    };
        $('.car_make').click(function(){
      var car_id =this.id;

      console.log(car_id)
      $('.car_make,#first-row').fadeOut(200,(function () {
        $('.'+car_id).fadeIn(1000)
    }));
        $('.'+car_id).click(function () {
            var model_id=this.id;
            $.ajax({
                url:"https://api.mlab.com/api/1/databases/car_models/collections/cars?apiKey=nLpPIkExIzD45P9OyqCYrLS8JVtpBHlS",
                type:"GET",
                data:{ get_param: 'value' },
                dataType:'json',
                success:function(data,responseText, statusTxt, xhr){
                    if(statusTxt == "success")
                        var parsedData =$.parseJSON(data)
                    // $('.'+car_id).on("click",function(){
                        $("."+car_id).fadeOut(1000)
                        $('#final-message').fadeIn(2000,function () {
                            $('#final-message').append( document.createTextNode( "Your car is a "+car_id+" "+model_id+" "+data[0]["make"][car_id]["models"][model_id]["category"] ) )

                        })

                    // })
                        console.log(data[0]["make"][car_id]["models"][model_id]["category"])

                    if(statusTxt == "error")
                        alert("Error: " + xhr.status + ": " + xhr.statusText);
    }

        })
        });

    })

})