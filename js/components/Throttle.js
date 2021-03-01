class Throttle {
    constructor(fn,time) {
        this.previousCall = null;
        this.lastCall = null;
        this.fn = fn;
        this.time = time;
        this.lastCallTimer = null;
    }
    call  (args)  {
        this.previousCall = this.lastCall;
        this.lastCall = Date.now();
        if(this.previousCall && (this.lastCall - this.previousCall) <= this.time) {
            clearTimeout(this.lastCallTimer);
        }
        this.lastCallTimer = setTimeout(() => {
            return this.fn(args)
        }, this.time);
    }
}
