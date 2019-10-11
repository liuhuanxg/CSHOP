window.onload=function (ev) {
    var f=function(){
        // console.log(111);
        var goods_id = $("#goods_id").val();
        console.log(goods_id);
        var data = $.ajax({
            url:"/seller/evaluation/"+goods_id,
            data:{goods_id:goods_id},
            dataType:"json",
            type:"GET",
            success:function (result) {
                if (result.flag==1){ Myecharts(result.data)}
                else{
                    console.log(111)
                }
            }
        })
    };
    f();
    var Mychart = echarts.init(document.getElementById("main"));
    function Myecharts(data){
        option = {
            backgroundColor:'#2c343c',//背景颜色
            title:{
                text:'评价占比',    //标题
                left:'center',      //标题水平位置
                top:100,             //标题垂直位置
                textStyle:{
                    color:'#ccc'//字体颜色
                }
            },
            tooltip:{
                trigger:'item',
                formatter:"{a}<br/>{b}:{c}({d}%)"
            },
            visualMap:{   //左下角颜色选择范围
                show:true,  //true时显示，false时不显示
                min:80,
                max:600,
                inRange:{
                    colorLightness:[0,0.5]   //占比重的颜色
                }
            },
            series:[{
                name:"评分信息",
                type:"pie",
                radius:"55%",
                center:["50%","50%"],
                data:data.sort(function (a,b) {return a.value - b.value  }),
                roseType:'radius',
                label:{
                    normal:{
                        textStyle:{color:"rgba(255,255,255,0.3)"} //字体颜色
                    }
                },
                labelLine:{
                    normal:{lineStyle:{color:"rgba(255,255,255,0.3)"},//线条颜色
                    // smooth:0.2,
                    // // length:10,
                    // // length2:20
                    }
                },
                itemStyle:{
                    normal:{
                        color:"#c23531",
                        shadowBlur:200,
                        shadowColor:"rgba(0,0,0,0.5)"}
                        },
                // animationType:"scale",
                // animationEasing:"elasticOut",
                // animationDelay:function (idx) {
                //     return  Math.random()*200;
                // }
            }]
        };
        Mychart.setOption(option);}
 };


