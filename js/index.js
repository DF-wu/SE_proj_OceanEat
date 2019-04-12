$().ready(function () {
  let sketch = function(p) { makeCanvas(p, p.windowWidth, 250) };
  new p5(sketch, document.getElementById('footer'));
});

let yoff = 0.0;
function makeCanvas(p, w, h) {
  p.setup = function(){
    p.createCanvas(w - .5, h);
  }

  p.draw = function() {
    // p.background(176, 184, 189);
    p.clear();
    p.fill(0,119,200);
    p.noStroke();
    // We are going to draw a polygon out of the wave points
    p.beginShape();

    let xoff = 0; // Option #1: 2D Noise
    // let xoff = yoff; // Option #2: 1D Noise

    // Iterate over horizontal pixels
    for (let x = 0; x <= w + 5; x += 10) {
      // Calculate a y value according to noise, map to

      // Option #1: 2D Noise
      let y = p.map(p.noise(xoff, yoff), 0, 1, 50, 200);

      // Option #2: 1D Noise
      // let y = map(noise(xoff), 0, 1, 200,300);

      // Set the vertex
      p.vertex(x, y);
      // Increment x dimension for noise
      xoff += 0.05;
    }
    // increment y dimension for noise
    yoff += 0.01;
    p.vertex(w + 5, h);
    p.vertex(0, h);
    p.endShape(p.CLOSE);
  }
}