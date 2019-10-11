window.onload=function (ev) {
    var Mychart = echarts.init(document.getElementById("main"));
    Mychart.title = "坐标轴刻度与标签对齐";
    option = {
        color:["orange"],  //颜色，默认为黑色
        tooltip: {
            trigger: "axis",
            axisPointer: {      //坐标轴指示器；坐标轴触发有效
                type:"line"}    //鼠标移入的显示效果，默认为直线，可选为"line"| "shadow"
        },
        grid: {
            left:'30%',         //距离坐标的距离
            right:'40px',       //距离右边的距离
            bottom:'3%',        //距离下端的距离
            containLabel:false
        },
        xAxis:[  //横轴坐标
            {type:"category",
            data:["Mon","Tue","web","Thu","Fri","Sat","Sun"],  //横轴数据
            axiStick:{alignWithLabel:true}
            }],
        yAxis:[{type:"value"}], //y轴坐标
        series:[{name:"微信支付",type:"bar",barWidth:"60%",data:[10,52,200,334,390,330,220]}]  //y轴数据
    };
    Mychart.setOption(option)
};