class ShopList {
    constructor(container, counter,api) {
        this.container = container;
        this.counter = counter;
        this.api = api;
        this.delItem = this.delItem.bind(this)
    }
    addEvent(){
        this.container.addEventListener('click', this.delItem)
    }
    delItem (e) {
        const target = e.target;
        if(target.classList.contains('shopping-list__button')) {
            const item = target.closest('.shopping-list__item');
            this.api.removePurchases(item.getAttribute('data-id'))
                .then( e => {
                    item.remove();
                    this.counter.minusCounter();
                })
                .catch( e => {
                    console.log(e)
                })
        }
    }
}
