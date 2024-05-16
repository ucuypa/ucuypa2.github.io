let asciiFrames = [];
let currentFrame = 0;
let frameDuration = 30;  // Duration to display each frame (in milliseconds)
let lastFrameTime = 0;

function preload() {
  loadStrings('ascii_frames.txt', (result) => {
    asciiFrames = result.join('\n').split('\n\n');
  });
}

function setup() {
  createCanvas(windowWidth, windowHeight);
  textSize(10);
  textFont('monospace');
  fill(255);
  loop(); // Start continuous execution of draw()
}

function draw() {
  background(0);
  if (asciiFrames.length > 0) {
    let frame = asciiFrames[currentFrame];
    text(frame, 10, 10);
  }
  updateFrame();
}

function updateFrame() {
  let currentTime = millis();
  if (currentTime - lastFrameTime > frameDuration) {
    currentFrame = (currentFrame + 1) % asciiFrames.length;
    lastFrameTime = currentTime;
  }
}

function keyPressed() {
  if (keyCode === ENTER) {
    if (isLooping()) {
      noLoop();
    } else {
      loop();
    }
  }
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
}
