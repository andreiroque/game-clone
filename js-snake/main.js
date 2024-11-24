let s;

function setup() {
  createCanvas(400, 400);
  s = new Snake();
}

function draw() {
  background(0);
  s.show();
  s.update();
}
