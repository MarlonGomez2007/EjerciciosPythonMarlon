document.addEventListener('DOMContentLoaded', () => {
    const prices = {
        food: {
            'Selecciona': 0,
            'Hamburguesa': 10000,
            'Pizza': 12000,
            'Papas Fritas': 8000,
        },
        drink: {
            'Selecciona': 0,
            'Coca-Cola': 5000,
            'Jugo Natural': 6000,
            'Agua': 4000,
        }
    };

    const tableData = {
        table1: { totalFood: 0, countFood: 0, totalDrink: 0, countDrink: 0 },
        table2: { totalFood: 0, countFood: 0, totalDrink: 0, countDrink: 0 },
        table3: { totalFood: 0, countFood: 0, totalDrink: 0, countDrink: 0 },
        table4: { totalFood: 0, countFood: 0, totalDrink: 0, countDrink: 0 },
        table5: { totalFood: 0, countFood: 0, totalDrink: 0, countDrink: 0 },
    };

    function updateTotal(tableId) {
        const { totalFood, countFood, totalDrink, countDrink } = tableData[tableId];
        const total = totalFood + totalDrink;
        const count = countFood + countDrink;

        document.getElementById(`total${tableId.slice(-1)}`).textContent = `$${total}`;
        document.getElementById(`count${tableId.slice(-1)}`).textContent = count;
    }

    function updateTable(event) {
        const button = event.target;
        const tableId = button.dataset.table;
        const type = button.dataset.type;
        const select = document.querySelector(`.item-select[data-table="${tableId}"][data-type="${type}"]`);
        const item = select.options[select.selectedIndex].text;
        const itemName = item.split(' - ')[0];
        const itemPrice = prices[type][itemName];
        const operation = button.classList.contains('add-btn') ? 1 : -1;

        if (type === 'food') {
            if (operation === 1) {
                tableData[tableId].totalFood += itemPrice;
                tableData[tableId].countFood += 1;
            } else if (tableData[tableId].countFood > 0) {
                tableData[tableId].totalFood = Math.max(0, tableData[tableId].totalFood - itemPrice);
                tableData[tableId].countFood -= 1;
            }
        } else if (type === 'drink') {
            if (operation === 1) {
                tableData[tableId].totalDrink += itemPrice;
                tableData[tableId].countDrink += 1;
            } else if (tableData[tableId].countDrink > 0) {
                tableData[tableId].totalDrink = Math.max(0, tableData[tableId].totalDrink - itemPrice);
                tableData[tableId].countDrink -= 1;
            }
        }

        updateTotal(tableId);
    }

    function clearTotal(event) {
        const button = event.target;
        const tableId = button.dataset.table;
        tableData[tableId] = { totalFood: 0, countFood: 0, totalDrink: 0, countDrink: 0 };
        updateTotal(tableId);

        document.querySelectorAll(`.item-select[data-table="${tableId}"]`).forEach(select => {
            select.selectedIndex = 0;
        });
    }

    document.querySelectorAll('.add-btn, .subtract-btn').forEach(button => {
        button.addEventListener('click', updateTable);
    });

    document.querySelectorAll('.clear-btn').forEach(button => {
        button.addEventListener('click', clearTotal);
    });
});
