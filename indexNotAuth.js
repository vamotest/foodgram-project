const container = document.querySelector('.card-list');
const counterId = document.querySelector('#counter');
const api = new Api(apiUrl);
const header = new Header(counterId);
const configButton = {
    purchases: {
        attr: 'data-out',
        default: {
            class: 'button_style_light-blue',
            text: '<span class="icon-plus button__icon"></span>Добавить в покупки'
        },
        active: {
            class: 'button_style_light-blue-outline',
            text: `<span class="icon-check button__icon"></span> Рецепт добавлен`
        }
    }
}
const purchases = new Purchases(configButton.purchases, api);

const cardList = new CardList(container, '.card', header, api, false, {
    purchases
});

cardList.addEvent();


