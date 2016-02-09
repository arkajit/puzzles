var Meal = function(name) {
  this.name = name;
  this.dinerDishes = {};
};

var Dish = function(name, cost) {
  this.name = name;
  this.cost = cost;
};

Meal.prototype.getBill = function(tax, tip) {
  var bill = { 'total': 0.0 };

  for (var diner in this.dinerDishes) {
    var dinerTotal = 0.0;
    this.dinerDishes[diner].forEach(function(dish) {
      dinerTotal += dish.cost;
    });

    dinerTotal *= (1+tax) * (1+tip);
    bill[diner] = dinerTotal;
    bill['total'] += dinerTotal
  }

  return bill;
};

Meal.prototype.addDish = function(diner, dish) {
  var dishes = this.dinerDishes[diner] || [];
  dishes.push(dish);
  this.dinerDishes[diner] = dishes;
};

var chicken = new Dish('chicken', 9.99);
var eggplant = new Dish('eggplant', 13.99);
var soup = new Dish('soup', 3.49);
var salad = new Dish('salad', 5.49);
var soda = new Dish('soda', 1.49);
var beer = new Dish('beer', 6.49);

var m = new Meal('Dinner');
m.addDish('Alex', chicken)
m.addDish('Beth', salad)
m.addDish('Alex', soda)
m.addDish('Dave', soda)
m.addDish('Dave', eggplant)
m.addDish('Beth', soup)
m.addDish('Beth', beer);

console.log(m.getBill(0.1, 0.2));
