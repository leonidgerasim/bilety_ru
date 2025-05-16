document.addEventListener('DOMContentLoaded', func_list('id_originLocationCode', 'originList'));
document.addEventListener('DOMContentLoaded', func_list('id_destinationLocationCode', 'destinationList'));
function func_list(id_input, id_list) {
    const input = document.getElementById(id_input);
    const autocompleteList = document.getElementById(id_list);
    let currentFocus = -1;

    input.addEventListener('input', function(e) {
        const query = e.target.value;

        if (query.length < 2) {
            closeAllLists();
            return;
        }

        fetch(`/api_airport_search/?query=${encodeURIComponent(query)}`)
            .then(response => response.json())
            .then(data => {
                showSuggestions(data);
            });
    });

    input.addEventListener('keydown', function(e) {
        const items = autocompleteList.getElementsByTagName('div');

        if (e.keyCode === 40) {
            currentFocus++;
            addActive(items);
        } else if (e.keyCode === 38) {
            currentFocus--;
            addActive(items);
        } else if (e.keyCode === 13) { // Enter
            e.preventDefault();
            if (currentFocus > -1) {
                if (items) items[currentFocus].click();
            }
        }
    });

    function showSuggestions(items) {
        closeAllLists();
        currentFocus = -1;

        if (!items || items.length === 0) return;

        items.forEach(item => {
            const itemElement = document.createElement('div');
            itemElement.innerHTML = `<strong>${item.substr(0, input.value.length)}</strong>${item.substr(input.value.length)}`;
            itemElement.innerHTML += `<input type='hidden' value='${item}'>`;

            itemElement.addEventListener('click', function() {
                input.value = this.getElementsByTagName('input')[0].value;
                closeAllLists();
            });

            autocompleteList.appendChild(itemElement);
        });
    }

    function addActive(items) {
        if (!items) return false;

        removeActive(items);

        if (currentFocus >= items.length) currentFocus = 0;
        if (currentFocus < 0) currentFocus = (items.length - 1);

        items[currentFocus].classList.add('autocomplete-active');
    }

    function removeActive(items) {
        for (let i = 0; i < items.length; i++) {
            items[i].classList.remove('autocomplete-active');
        }
    }

    function closeAllLists() {
        const items = autocompleteList.getElementsByTagName('div');
        for (let i = 0; i < items.length; i++) {
            items[i].parentNode.removeChild(items[i]);
        }
    }

    document.addEventListener('click', function(e) {
        if (e.target !== input) {
            closeAllLists();
        }
    });

}
