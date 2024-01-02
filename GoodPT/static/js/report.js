
new WOW().init();
var data = {
  labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
  series: [
    [12242, 14627, 13111, 16723, 9814, 23421, 19782]
  ]
};
var options = {
  height: 300,
  showArea: true
};
new Chartist.Line('.ct-chart', data, options);

var data = {
  labels: ['Bluetooth', 'Apple', 'Tablet', 'Mouse', 'Hard Drive', 'Keyboard', 'USB', 'SSD', 'Laptop', 'Ghia'],
  series: [225, 76, 194, 188, 181, 177, 174, 158, 146, 110]
};

var options = {
  labelInterpolationFnc: function(value) {
    return value[0]
  }
};

var responsiveOptions = [
  ['screen and (min-width: 640px)', {
    chartPadding: 30,
    labelOffset: 100,
    labelDirection: 'explode',
    labelInterpolationFnc: function(value) {
      return value;
    }
  }],
  ['screen and (min-width: 1024px)', {
    labelOffset: 80,
    chartPadding: 20
  }]
];

new Chartist.Pie('.ct-chart-2', data, options, responsiveOptions);