window.onload = function() {
    // Get the canvas element
    const canvas = document.getElementById("webgl-canvas");
    
    // Setup WebGL context
    const gl = WebGLUtils.setupWebGL(canvas);
    if (!gl) return;

    // Set the viewport
    gl.viewport(0, 0, canvas.width, canvas.height);

    // Clear the canvas with cornflower blue
    gl.clearColor(0.3921, 0.5843, 0.9294, 1.0);
    gl.clear(gl.COLOR_BUFFER_BIT);
};
