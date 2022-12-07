let width = 800,
    height = 800;

let canvas = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height)
    .append("g")
    .attr("transform", "translate(50,50)");


d3.json("static/script/sample.json").then(function (data) {
    let sim = d3.forceSimulation()
        .force("x", d3.forceX(width / 2).strength(.05))
        .force("y", d3.forceY(height / 2).strength(.05))
        .force("collide", d3.forceCollide(60))

    let node = canvas.selectAll(".node")
        .data(data)
        .enter().append("circle")
        .attr("class", "node")
        .attr("r", d => d.Szam * 5)
        .attr("fill", "steelblue")
        .attr("opacity", 0.4)
        .attr("stroke", "#000")
        .attr("sroke-width", "2")


    let labels = canvas.selectAll(".labels")
        .data(data)
        .enter().append("text")
        .attr("class", "labels")
        .attr("text-anchor", "middle")
        .attr("fill", "black")
        .text(d => d.Name + " " + d.Szam)

    sim.nodes(data).on('tick', ticked)

    function ticked() {
        labels
            .attr("x", d => d.x)
            .attr("y", d => d.y)
        node
            .attr("cx", d => d.x)
            .attr("cy", d => d.y)
    }
})

//d3.json("/graph-data").then((data) => initGraph(data.Name, data.Szam));

/*, function (data) {
    let nodes = pack.nodes(data);

    let node = canvas.selectAll(".node")
        .data(nodes)
        .enter()
        .append("g")
        .attr("class", "node")
        .attr("transform", function (d) {
            return "translate(" + d.x + "," + d.y + ")";
        });

    node.append("circle")
        .attr("r",function (d) {
            return d.r;
        })
        .attr("fill","steelblue")
        .attr("opacity",0.25)
        .attr("stroke","#ADADAD")
        .attr("sroke-width","2");

    node.append("text")
        .text(function (d) {
            return d.Name
        })
}*/

