export class Block {
    constructor( width, height, x, y ) {
    this.width = width;
    this.height = height;
    this.x = x;
    this.y = y;
    this.maxX = this.width + x;
    this.maxY = this.height + y;
    }
    
    draw(ctx) {
    
    const xGap = 30;
    const yGap = 10;
    
    ctx.fillStyle = '#7c7e97';
    ctx.beginPath();
    ctx.rect(this.x, this.y, this.width, this.height);
    ctx.fill();

    ctx.fillStyle = '#190f3a';
    ctx.beginPath();
    ctx.moveTo(this.maxX, this.maxY);
    ctx.lineTo(this.maxX - xGap, this.maxY + yGap);
    ctx.lineTo(this.x - xGap, this.maxY + yGap);
    ctx.lineTo(this.x, this.y + yGap);
    ctx.fill();

    ctx.fillStyle = '#efeff5';
    ctx.beginPath();
    ctx.moveTo(this.x - xGap, this.y + yGap + yGap);
    ctx.lineTo(this.x - xGap, this.y + yGap);
    ctx.lineTo(this.x, this.y);
    ctx.lineTo(this.x,this.y + yGap);
    ctx.fill();
    }
}