class Purchases {
    constructor(config, api) {
        this.config = config;
        this.api = api;
        this.addPurchases = this.addPurchases.bind(this)
    }
    addPurchases (target,cardId, callBack) {
        target.setAttribute('disabled', true);
        this.api.addPurchases(cardId)
            .then( e => {
                target.innerHTML = this.config.active.text;
                target.classList.remove(this.config.default.class);
                target.classList.add(this.config.active.class);
                target.removeAttribute(this.config.attr);
                callBack&&callBack();
            })
            .catch( e => {
                console.log(e)
            })
            .finally(e => {
                target.removeAttribute('disabled');
            })
    };
    removePurchases (target,cardId,callBack) {
        target.setAttribute('disabled', true)
        this.api.removePurchases(cardId)
            .then( e => {
                target.innerHTML = this.config.default.text;
                target.classList.add(this.config.default.class);
                target.classList.remove(this.config.active.class);
                target.setAttribute(this.config.attr, true);
                callBack&&callBack();
            })
            .catch( e => {
                console.log(e)
            })
            .finally(e => {
                target.removeAttribute('disabled');

            })
    };
}
