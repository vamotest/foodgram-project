class MainCards {
    constructor(container, card, counter, api, userAuth,button) {
        this.container = container;
        this.card = card;
        this.userAuth = userAuth;
        this.counter = counter;
        this.target = null;
        this.button = button;
        this._eventUserAuth = this._eventUserAuth.bind(this);
        this._eventUserNotAuth = this._eventUserNotAuth.bind(this);

    }
    addEvent() {
        const eventCb = this._access();
        this.container.addEventListener('click', eventCb)
    }
    _access () {
        if(this.userAuth) {
            return this._eventUserAuth;
        } else {
            return this._eventUserNotAuth;
        }
    }
    _eventUserAuth (e) {
        this.target = e.target.closest('button');
    }
    _eventUserNotAuth (e) {
        this.target = e.target.closest('button');
    }
}
