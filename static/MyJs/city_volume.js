window.onload=function (ev) {
    function f() {
        var c_id =$("#c_id").val();
        var data = $.ajax( {
            url:"/seller/city_volume/"+c_id,
            data:{c_id:c_id},
            dataType:"json",
            type:"GET",
            success:function (result) {
                if(result.flag ==1){
                    myecharts(result.data)
                }
            }
        })
    }
    f();
    function myecharts(data) {
        var Mychart =  echarts.init(document.getElementById("main"));
        var builderJson = data;


        var downloadJson = data.charts;

        var themeJson = data.components;

        var waterMarkText = 'ECHARTS';

        var canvas = document.createElement('canvas');
        var ctx = canvas.getContext('2d');
        canvas.width = canvas.height = 100;
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.globalAlpha = 0.08;
        ctx.font = '20px Microsoft Yahei';
        ctx.translate(50, 50);
        ctx.rotate(-Math.PI / 4);
        ctx.fillText(waterMarkText, 0, 0);

        option = {
            backgroundColor: {
                type: 'pattern',
                image: canvas,
                repeat: 'repeat'
            },
            tooltip: {},
            title: [{
                text: '河南省销售额',
                subtext: '总计 ' + builderJson.all,
                x: '25%',
                textAlign: 'center'
            }, {
                text: '河南省各市营业额占比',
                subtext: '总计 ' + Object.keys(downloadJson).reduce(function (all, key) {
                    return all + downloadJson[key];
                }, 0),
                x: '75%',
                textAlign: 'center'
            }, {
                text: '河北省营业额',
                subtext: '总计 ' + Object.keys(themeJson).reduce(function (all, key) {
                    return all + themeJson[key];
                }, 0),
                x: '75%',
                y: '50%',
                textAlign: 'center'
            }],
            grid: [{
                top: 50,
                width: '50%',
                bottom: '45%',
                left: 10,
                containLabel: true
            }, {
                top: '55%',
                width: '50%',
                bottom: 0,
                left: 10,
                containLabel: true
            }],
            xAxis: [{
                type: 'value',
                max: builderJson.all,
                splitLine: {
                    show: false
                }
            }, {
                type: 'value',
                max: builderJson.all,
                gridIndex: 1,
                splitLine: {
                    show: false
                }
            }],
            yAxis: [{
                gridIndex:0,
                type: 'category',
                data: Object.keys(builderJson.charts),
                axisLabel: {
                    interval: 0,
                    rotate: 30
                },
                splitLine: {
                    show: false
                }
            }, {
                gridIndex: 1,
                type: 'category',
                data: Object.keys(builderJson.components),
                axisLabel: {
                    interval: 0,
                    rotate: 30
                },
                splitLine: {
                    show: false
                }
            }],
            series: [{
                type: 'bar',
                stack: 'chart',
                z: 3,
                label: {
                    normal: {
                        position: 'right',
                        show: true
                    }
                },
                data: Object.keys(builderJson.charts).map(function (key) {
                    return builderJson.charts[key];
                })
            }, {
                type: 'bar',
                stack: 'chart',
                silent: true,
                itemStyle: {
                    normal: {
                        color: '#eee'
                    }
                },
                data: Object.keys(builderJson.charts).map(function (key) {
                    return builderJson.all - builderJson.charts[key];
                })
            }, {
                type: 'bar',
                stack: 'component',
                xAxisIndex: 1,
                yAxisIndex: 1,
                z: 3,
                label: {
                    normal: {
                        position: 'right',
                        show: true
                    }
                },
                data: Object.keys(builderJson.components).map(function (key) {
                    return builderJson.components[key];
                })
            }, {
                type: 'bar',
                stack: 'component',
                silent: true,
                xAxisIndex: 1,
                yAxisIndex: 1,
                itemStyle: {
                    normal: {
                        color: '#eee'
                    }
                },
                data: Object.keys(builderJson.components).map(function (key) {
                    return builderJson.all - builderJson.components[key];
                })
            }, {
                type: 'pie',
                radius: [0, '30%'],
                center: ['75%', '25%'],
                data: Object.keys(downloadJson).map(function (key) {
                    return {
                        name: key.replace('.js', ''),
                        value: downloadJson[key]
                    }
                })
            }, {
                type: 'pie',
                radius: [0, '30%'],
                center: ['75%', '75%'],
                data: Object.keys(themeJson).map(function (key) {
                    return {
                        name: key.replace('.js', ''),
                        value: themeJson[key]
                    }
                })
            }]
        };
            Mychart.setOption(option);
        }
    };
