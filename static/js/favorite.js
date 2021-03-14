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
    },
    favorites: {
        attr: 'data-out',
        default: {
            class: ['button', 'button_style_none'],
            text: '<span class="icon-favorite"></span>'
        },
        active: {
            class: '.icon-favorite_active',
            text: `<span class="icon-favorite icon-favorite_active"></span>`
        }
    }
}
const purchases = new Purchases(configButton.purchases, api);
const favorites = new Favorites(configButton.favorites, api);

const cardList = new CardList(container, '.card', header, api, true, {
    purchases,
    favorites
});

cardList.addEvent();


