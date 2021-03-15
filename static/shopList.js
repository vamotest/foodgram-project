const container = document.querySelector('.shopping-list');
const counterId = document.querySelector('#counter');
const api = new Api(apiUrl);
const header = new Header(counterId);

const shopList = new ShopList(container, header, api);
shopList.addEvent();
