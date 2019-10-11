window.onload=function (ev) {
    var Mychart = echarts.init(document.getElementById("main"));
    //使用ajax向后端发起请求
    function f(){
        var q_id = $("#q_id").val();
        console.log(q_id);
        var data = $.ajax({
            url:"/seller/show_quarter/"+q_id,
            dataType:"json",
            type:"get",
            data:{"q_id":q_id},
            success:function (result) {
                if(result.flag == 1){
                    Mycharts(result.data);
                }
                else{
                    window.alert(result.data);
                }
            }
        })
    }
    f();
    var timeId = setInterval(f,1000); //设置定时器，一秒钟执行一次
    function Mycharts(data){
        option = {
        title:{
            text:"各季度营业额",
            left:"center",
            top:20.,
            textStyle:{color:"black"}
        },
        tooltip:{
            trigger:"item",
            formatter:"{a}<br/>{b}:{c}({d}%)"
        },
        legend:{
            orient:"vertical",
            x:"left",
            // data:['直达','营销广告','搜索引擎','邮件营销','联盟广告','视频广告','百度','谷歌','必应','其他']
        },
        series:[
            {
            name:"营业额",
            type:"pie",
            selectedMode:"single",
            radius:[0,"30%"],
            label:{normal:{position:"inner"}},
            labelLine:{normal:{show:false}},
            data:data.quarter_data
            },
            {
            name:"营业额",
            type:"pie",
            radius:["40%","55%"],
            label:{
                normal:{
                    formatter:"{a|{a}}{abg|}\n{hr|}\n {b|{b}:}{c}  {per|{d}%}   ",
                    backgroundColor:"#eee",
                    borderWidth:1,
                    borderRadius:4,
                    rich:{
                        a:{
                            color:"#999",
                            lineHeight:22,
                            align:"center"
                        },
                        hr:{
                            borderColor:"#aaa",
                            width:"100%",
                            borderWidth:0.5,
                            height:0
                        },
                        per:{
                            color:"#eee",
                            backgroundColor:"#334455",
                            padding:[2,4],
                            borderRadius:2
                        }
                    }
                }
            },
            data:data.month_data
            }
        ]
    };
    Mychart.setOption(option)
    }

};
