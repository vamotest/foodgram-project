class Api {
  constructor(apiUrl) {
    this.apiUrl = apiUrl;
  }

  async getPurchases() {
    const e = await fetch(`${this.apiUrl}/purchases/`, {
      headers: {
        'Content-Type': 'application/json',
      }
    });
    if (e.ok) {
      return e.json();
    }
    return await Promise.reject(e.statusText);
  }

  async addPurchases(id) {
    const e = await fetch(`${this.apiUrl}/purchases/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
      },
      body: JSON.stringify({
        recipe: id
      })
    });
    if (e.ok) {
      return e.json();
    }
    return await Promise.reject(e.statusText);
  }

  async removePurchases(id) {
    const e = await fetch(`${this.apiUrl}/purchases/${id}/`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
      }
    });
    if (e.ok) {
      return e.json();
    }
    return await Promise.reject(e.statusText);
  }

  async addSubscriptions(id) {
    const e = await fetch(`${this.apiUrl}/subscriptions/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
      },
      body: JSON.stringify({
        author: id,
      })
    });
    if (e.ok) {
      return e.json();
    }
    return await Promise.reject(e.statusText);
  }

  async removeSubscriptions(id) {
    const e = await fetch(`${this.apiUrl}/subscriptions/${id}/`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
      }
    });
    if (e.ok) {
      return e.json();
    }
    return await Promise.reject(e.statusText);
  }

  async addFavorites(id) {
    const e = await fetch(`${this.apiUrl}/favorites/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
      },
      body: JSON.stringify({
        recipe: id
      })
    });
    if (e.ok) {
      return e.json();
    }
    return await Promise.reject(e.statusText);
  }

  async removeFavorites(id) {
    const e = await fetch(`${this.apiUrl}/favorites/${id}/`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
      }
    });
    if (e.ok) {
      return e.json();
    }
    return await Promise.reject(e.statusText);
  }
  
  async getIngredients(text) {
    const e = await fetch(`${this.apiUrl}/ingredients/?search=${text}`, {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    if (e.ok) {
      return e.json();
    }
    return await Promise.reject(e.statusText);
  }
}
