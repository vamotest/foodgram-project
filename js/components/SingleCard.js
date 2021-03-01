class SingleCard extends MainCards{
    constructor(container, card, counter, api, userAuth,button) {
        super(container, card, counter, api, userAuth,button);
        this.tooltipAdd = this.tooltipAdd.bind(this);
        this.tooltipDel = this.tooltipDel.bind(this)
    }
    _eventUserAuth (e) {
        super._eventUserAuth(e);
        if (this.target && this.target.name === 'purchases') {
            this._eventPurchases(this.target)
        }
        if (this.target && this.target.name === 'favorites') {
            this._eventFavorites(this.target);
        }
        if (this.target && this.target.name === 'subscribe') {
            this._eventSubscribe(this.target)
        }
    }
    _eventUserNotAuth  (e)  {
        super._eventUserAuth(e);
        if (this.target && this.target.name === 'purchases') {
            this._eventPurchases(this.target)
        }
    }
    _eventSubscribe  (target)  {
        const authorId = target.closest(this.card).getAttribute('data-author');
        if(target.hasAttribute('data-out')) {
            this.button.subscribe.addSubscribe(target, authorId)
        } else {
            this.button.subscribe.removeSubscribe(target,authorId)
        }
    }
    _eventFavorites  (target)  {
        const cardId = target.closest(this.card).getAttribute('data-id');
        if(target.hasAttribute('data-out')) {
            this.button.favorites.addFavorites(target,cardId, this.tooltipDel)
        } else {
            this.button.favorites.removeFavorites(target,cardId, this.tooltipAdd)
        }
    }
    tooltipAdd  () {
        const item = this.target.closest('.single-card').querySelector('.single-card__favorite-tooltip');
        item.textContent = "Добавить в избранное"
    }
    tooltipDel () {
        const item = this.target.closest('.single-card__favorite').querySelector('.single-card__favorite-tooltip');
        item.textContent = "Убрать из избранного"
    }
    _eventPurchases  (target)  {
        const cardId = target.closest(this.card).getAttribute('data-id');
        if(target.hasAttribute('data-out')) {
            this.button.purchases.addPurchases(target,cardId,this.counter.plusCounter)
        } else {
            this.button.purchases.removePurchases(target,cardId,this.counter.minusCounter)
        }
    }
}

