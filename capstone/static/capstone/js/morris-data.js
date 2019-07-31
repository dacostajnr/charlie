$(document).ready(

        function(){           
        // definle global variable 
        var list=[];
        // create a morris for this list
        function f4(){
                        if (list.length!=0){
            for (var i=0;i<list["data"].length;i++){ 
            var current_name=list["data"][i]["name"]
            var current_tag_id=$("#"+current_name)        
            Morris.Line(
                {
                    element:current_tag_id,
                    data:list["data"][i]["times"],
                    xkey: "time",
                    ykeys:["value"], 
                    labels:["Value"],
                    smooth: true,
                    hideHover:false,
                    resize:true,
                    }
                );
            }
            }

        else{
            console.log("nothing here");
        }
        }


function f2(){ 
    //draw graph once     
    console.log("f2 called");
    $.ajax({
            url:"/ajax/",
            data:{"type":"fetch_values"},
            dataType:"json",
                success:function(data){
                    console.log("data received");                                                                         
                    list = data;
                    f4();
                }
            });   
        }  

            setInterval(f2,1000);            
        }
    ); 



