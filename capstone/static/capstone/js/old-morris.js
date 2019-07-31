//draw graph once 
    $.ajax({
            url:"/ajax/",
            data:{"type":"fetch_values"},
            dataType:"json",
                success:function(data){                  
                    for (var i=0;i<data["data"].length;i++){
                        var current_name=data["data"][i]["name"]
                        var current_tag_id=$("#"+current_name)
                        //---------------graph--------------
                        maingraph= Morris.Line(
                                {
                                    element:current_tag_id,
                                    data:data["data"][i]["times"],
                                    xkey: "time",
                                    ykeys:["value"], 
                                    labels:["Value"],
                                    smooth: true,
                                    hideHover:false,
                                    resize:false,
                                }
                            );
                        //---------------graph--------------                                                
                    }
                    
                    
                }
            });   

