class Header {
    constructor(counter) {
        this.counter = counter;
        this.api = api;
        this.counterNum = this.counter.textContent;
        this.plusCounter = this.plusCounter.bind(this);
        this.minusCounter = this.minusCounter.bind(this);
    }

    plusCounter  ()  {
        this.counterNum = ++this.counterNum;
        this.counter.textContent = this.counterNum;
    }
    minusCounter ()  {
        this.counterNum = --this.counterNum;
        this.counter.textContent = this.counterNum;
    }
}
