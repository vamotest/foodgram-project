class Subscribe {
    constructor(config, api) {
        this.config = config;
        this.api = api;
    }
    addSubscribe (target, authorId) {
        target.setAttribute('disabled', true)
        this.api.addSubscriptions(authorId)
            .then( e => {
                target.innerHTML = this.config.active.text;
                target.classList.remove(this.config.default.class);
                target.classList.add(this.config.active.class);
                target.removeAttribute(this.config.attr);
            })
            .catch( e => {
                console.log(e)
            })
            .finally(e => {
                target.removeAttribute('disabled');
            })
    };
    removeSubscribe (target, authorId) {
        target.setAttribute('disabled', true)
        this.api.removeSubscriptions(authorId)
            .then( e => {
                target.innerHTML = this.config.default.text;
                target.classList.add(this.config.default.class);
                target.classList.remove(this.config.active.class);
                target.setAttribute(this.config.attr, true);
            })
            .catch( e => {
                console.log(e)
            })
            .finally(e => {
                target.removeAttribute('disabled');
            })
    };
}
