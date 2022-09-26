class App {
    constructor() {
        this.canvas = document.getElementById('ballBounce');
        this.ctx = this.canvas.getContext('2d');
        
        this.stageWidth = document.body.clientWidth;
        this.stageHeight = document.body.clientHeight;
        
        this.canvas.width = this.stageWidth;
        this.canvas.height = this.stageHeight;
        
        window.requestAnimationFrame(this.animate)
    }
    animate = () => {
    window.requestAnimationFrame(this.animate);
    }
}
window.onload = () => {
    new App();
};