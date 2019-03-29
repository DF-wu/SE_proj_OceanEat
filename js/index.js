function setup() {
    createCanvas($('body').width(), $('body').height());
  }
  
  function draw() {
    background(0)
    if (mouseIsPressed) {
        fill(125);
    } else {
        fill(255);
    }
    ellipse(mouseX, mouseY, 80, 80);
  }