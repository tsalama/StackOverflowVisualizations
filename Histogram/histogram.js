var width = document.getElementById('vis')
     .clientWidth;
var height = document.getElementById('vis')
     .clientHeight;

var margin = {
    top: 50,
    left: 50,
    right: 50,
    bottom: 40
};

var div = d3.select("body").append("div")   
    .attr("class", "tooltip")               
    .style("opacity", 0)

var svg = d3.select("#vis")
    .append("svg")
    .attr('width', width)
    .attr('height', height)
    .append("g")
    .attr("transform", "translate(" + margin.top + "," + margin.left + ")");

width = width - margin.left - margin.right;
height = height - margin.top - margin.bottom;

var duration = 1000;

var color_scale = d3.scaleLinear()
    .range(["#E0E0E0", "black"]);

var max_value = d3.select('#maxFreq')
    .node()
    .value;

var xscale = d3.scaleBand()
    .range([0, width])
    .padding(0.1);

var yscale = d3.scaleLinear()
    .range([height, 0])
    .domain([0, max_value]);

var xaxis = d3.axisBottom(xscale);

var yaxis = d3.axisLeft(yscale);

svg.append('g')
    .attr('transform', 'translate(0, ' + (height) + ')')
    .attr('class', 'x axis');

svg.append("text")             
  .attr("transform",
        "translate(" + (width/2) + " ," + 
                       (height + margin.top + 20) + ")")
  .style("text-anchor", "middle")
  .text("Value"); 

svg.append('g')
    .attr('class', 'y axis');

svg.append("text")
  .attr("transform", "rotate(-90)")
  .attr("y", 0 - margin.left)
  .attr("x",0 - (height / 2))
  .attr("dy", "1em")
  .style("text-anchor", "middle")
  .text("Frequency");   

function updateType(typ) {
    att = document.getElementById("attribute");
    update(typ, att.options[att.selectedIndex].value);
}

function updateAtt(att) {
    typ = document.getElementById("type");
    update(typ.options[typ.selectedIndex].value, att);
}

function update(typ, att) {
    d3.csv(typ + '_' + att + '_frequency.csv', function(csv_data) {
        var t = d3.transition()
            .duration(1500);

        var bins = csv_data.map(function(d) {
            return d.value;
        });
        xscale.domain(bins);

        csv_data.forEach(function(d) {
            d.value = d.value;
            d.frequency = parseInt(d.frequency);
        });

        var max_value = d3.max(csv_data, function(d) { return d.frequency; });

        yscale.domain([0, max_value]);

        color_scale.domain([0, max_value]);

        SetMax(max_value);

        var bars = svg.selectAll('.bar')
            .data(csv_data);

        console.log(max_value);

        //enter
        var new_bars = bars
            .enter()
            .append('rect')
            .attr('class', 'bar')
            .attr("fill", 'black')
            .attr('width', xscale.bandwidth())
            .attr('height', 0)
            .attr('y', height)
                    .on("mouseover", function(d) {      
            div.transition()        
                .duration(200)      
                .style("opacity", .9);      
            div .html("Value: <b>" + d.value + "</b><br/>"  + "Frequency: <b>" + d.frequency + "</b>")  
                .style("left", (d3.event.pageX) + "px")     
                .style("top", (d3.event.pageY - 28) + "px");    
            })                  
        .on("mouseout", function(d) {       
            div.transition()        
                .duration(500)      
                .style("opacity", 0);   
        });

        //update
        new_bars.merge(bars)
            .transition()
            .attr('x', function(d) {
                return xscale(d.value);
            })
            .attr('y', function(d) {
                return yscale(d.frequency);
            })
            .attr('height', function(d) {
                return height - yscale(d.frequency);
            })
            .attr("width", xscale.bandwidth())
            .attr('fill', function(d) {
                return color_scale(d.frequency);
            });              

        bars
            .exit()
            .transition()
            .duration(duration)
            .attr('height', 0)
            .attr('y', height)
            .remove();

        svg.select('.x.axis')
            .transition()
            .duration(duration)
            .call(xaxis);

        svg.select('.y.axis')
            .transition()
            .duration(duration)
            .call(yaxis);

    });
}

function maxFrequency() {
    attr = document.getElementById("attribute");
    att = attr.options[attr.selectedIndex].value;

    ty = document.getElementById("type");
    typ = ty.options[ty.selectedIndex].value;

    d3.csv(typ + '_' + att + '_frequency.csv', function(csv_data) {
        var t = d3.transition()
            .duration(1500);

        var bins = csv_data.map(function(d) {
            return d.value;
        });
        xscale.domain(bins);

        csv_data.forEach(function(d) {
            d.value = d.value;
            d.frequency = parseInt(d.frequency);
        });    

        max_value = d3.select('#maxFreq')
            .node()
            .value;
            
        yscale.domain([0, max_value]);

        color_scale.domain([0, max_value]);

        var bars = svg.selectAll('.bar')
            .data(csv_data);

        SetVal(max_value)

        //enter
        var new_bars = bars
            .enter()
            .append('rect')
            .attr('class', 'bar')
            .attr("fill", 'black')
            .attr('width', xscale.bandwidth())
            .attr('height', 0)
            .attr('y', height)

        //update
        new_bars.merge(bars)
            .transition()
            .attr('x', function(d) {
                return xscale(d.value);
            })
            .attr('y', function(d) {
                return yscale(d.frequency);
            })
            .attr('height', function(d) {
                return height - yscale(d.frequency);
            })
            .attr("width", xscale.bandwidth())
            .attr('fill', function(d) {
                return color_scale(d.frequency);
            });  

        bars
            .exit()
            .transition()
            .duration(duration)
            .attr('height', 0)
            .attr('y', height)
            .remove();

        svg.select('.x.axis')
            .transition()
            .duration(duration)
            .call(xaxis);

        svg.select('.y.axis')
            .transition()
            .duration(duration)
            .call(yaxis);

    });
}

function topsort() {
    attr = document.getElementById("attribute");
    att = attr.options[attr.selectedIndex].value;

    ty = document.getElementById("type");
    typ = ty.options[ty.selectedIndex].value;

    d3.csv("top" + typ + '_' + att + '_frequency.csv', function(csv_data) {
        var t = d3.transition()
            .duration(1500);

        var bins = csv_data.map(function(d) {
            return d.value;
        });
        xscale.domain(bins);

        csv_data.forEach(function(d) {
            d.value = d.value;
            d.frequency = parseInt(d.frequency);
        });

        max_value = d3.select('#maxFreq')
            .node()
            .value;
            
        yscale.domain([0, max_value]);
        
        color_scale.domain([0, max_value]);

        var bars = svg.selectAll('.bar')
            .data(csv_data);

        SetVal(max_value)

        //enter
        var new_bars = bars
            .enter()
            .append('rect')
            .attr('class', 'bar')
            .attr("fill", 'black')
            .attr('width', xscale.bandwidth())
            .attr('height', 0)
            .attr('y', height)

        //update
        new_bars.merge(bars)
            .transition()
            .attr('x', function(d) {
                return xscale(d.value);
            })
            .attr('y', function(d) {
                return yscale(d.frequency);
            })
            .attr('height', function(d) {
                return height - yscale(d.frequency);
            })
            .attr("width", xscale.bandwidth())
            .attr('fill', function(d) {
                return color_scale(d.frequency);
            });            

        bars
            .exit()
            .transition()
            .duration(duration)
            .attr('height', 0)
            .attr('y', height)
            .remove();

        svg.select('.x.axis')
            .transition()
            .duration(duration)
            .call(xaxis);

        svg.select('.y.axis')
            .transition()
            .duration(duration)
            .call(yaxis);

    });    
}

function SetMax (max) {
    var slider = document.getElementById ("maxFreq");

    if ('max' in slider) {  
        slider.max = max;
        slider.value = max;
    } else {
        slider.setAttribute ("max", max);
        slider.setAttribute ("value", max);
    }

    OnSliderChanged (slider);
}

function SetVal (max) {
    var slider = document.getElementById ("maxFreq");

    if ('max' in slider) {  
        slider.value = max;
    } else {
        slider.setAttribute ("value", max);
    }

    OnSliderChanged (slider);
}

function OnSliderChanged (slider) {
    var sliderValue = document.getElementById ("val");
    sliderValue.innerHTML = slider.value;
}

var output = document.getElementById ("val");

document.getElementById ("maxFreq").oninput = function() {
    output.innerHTML = this.value;
}

var select_type = d3.select('#type');
select_type.on('change', function() {
    updateType(this.value);
})

var select_att = d3.select('#attribute');
select_att.on('change', function() {
    updateAtt(this.value);
})

update('questions', 'char');