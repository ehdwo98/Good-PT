
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

// $(document).ready(function() {
//   $('#savePdf').click(function() { // pdf저장 button id
      
//       html2canvas($('#pdfCanvas')[0]).then(function(canvas) { //저장 영역 div id
      
//       // 캔버스를 이미지로 변환
//       var imgData = canvas.toDataURL('image/png');
           
//       var imgWidth = 190; // 이미지 가로 길이(mm) / A4 기준 210mm
//       var pageHeight = imgWidth * 1.414;  // 출력 페이지 세로 길이 계산 A4 기준
//       var imgHeight = canvas.height * imgWidth / canvas.width;
//       var heightLeft = imgHeight;
//       var margin = 10; // 출력 페이지 여백설정
//       var doc = new jsPDF('p', 'mm');
//       var position = 0;
         
//       // 첫 페이지 출력
//       doc.addImage(imgData, 'PNG', margin, position, imgWidth, imgHeight);
//       heightLeft -= pageHeight;
           
//       // 한 페이지 이상일 경우 루프 돌면서 출력
//       while (heightLeft >= 20) {
//           position = heightLeft - imgHeight;
//           doc.addPage();
//           doc.addImage(imgData, 'PNG', 0, position, imgWidth, imgHeight);
//           heightLeft -= pageHeight;
//       }
//       // 파일 저장
//       doc.save('report.pdf');
//       });
//   });
// })

$(document).ready(function() {
  $("#savePdf").click(function() { // pdf저장 button id

      setTimeout(function() {
        createPdf();
      }, 100);
  });
});

var renderedImg = new Array;

var contWidth = 200, // 너비(mm) (a4에 맞춤)
    padding = 5; //상하좌우 여백(mm)
var margin = 30; // 출력 페이지 여백설정

function createPdf() { //이미지를 pdf로 만들기
  // document.getElementById("loading").style.display = "block"; // 로딩 이미지 보이기

  var lists = document.querySelectorAll(".pdf_page"),
      deferreds = [],
      doc = new jsPDF("p", "mm", "a4"),
      listsLeng = lists.length;

  for (var i = 0; i < listsLeng; i++) { // pdf_page 적용된 태그 개수만큼 이미지 생성
    var deferred = $.Deferred();
    deferreds.push(deferred.promise());
    generateCanvas(i, doc, deferred, lists[i]);
  }

  $.when.apply($, deferreds).then(function () { // 이미지 렌더링이 끝난 후
    var sorted = renderedImg.sort(function(a,b){return a.num < b.num ? -1 : 1;}), // 순서대로 정렬
        curHeight = 90, //위 여백 (이미지가 들어가기 시작할 y축)
        sortedLeng = sorted.length;

    for (var i = 0; i < sortedLeng; i++) {
      var sortedHeight = sorted[i].height, //이미지 높이
          sortedImage = sorted[i].image; //이미지

      if(i===0) {
        doc.addImage(sortedImage, 'jpeg', padding , curHeight, contWidth, sortedHeight); //이미지 넣기
        curHeight += sortedHeight; // y축 = 여백 + 새로 들어간 이미지 높이
      }
      else {
        if( curHeight + sortedHeight > 297 - padding * 2 ){ // a4 높이에 맞게 남은 공간이 이미지높이보다 작을 경우 페이지 추가
          doc.addPage(); // 페이지를 추가함
          curHeight = margin; // 이미지가 들어갈 y축을 초기 여백값으로 초기화
          doc.addImage(sortedImage, 'jpeg', padding , curHeight, contWidth, sortedHeight); //이미지 넣기
          curHeight += sortedHeight; // y축 = 여백 + 새로 들어간 이미지 높이
        } else { // 페이지에 남은 공간보다 이미지가 작으면 페이지 추가하지 않음
          doc.addImage(sortedImage, 'jpeg', padding , curHeight, contWidth, sortedHeight); //이미지 넣기
          curHeight += sortedHeight; // y축 = 기존y축 + 새로들어간 이미지 높이
        }
      }
      
    }
    doc.save('Report.pdf'); //pdf 저장

    curHeight = margin; //y축 초기화
    renderedImg = new Array; //이미지 배열 초기화
  });
}

function generateCanvas(i, doc, deferred, curList){ //페이지를 이미지로 만들기
  var pdfWidth = $(curList).outerWidth() * 0.2645, //px -> mm로 변환
      pdfHeight = $(curList).outerHeight() * 0.2645,
      heightCalc = contWidth * pdfHeight / pdfWidth; //비율에 맞게 높이 조절
  html2canvas( curList ).then(
    function (canvas) {
      var img = canvas.toDataURL('image/jpeg', 1.0); //이미지 형식 지정
      renderedImg.push({num:i, image:img, height:heightCalc}); //renderedImg 배열에 이미지 데이터 저장(뒤죽박죽 방지)     
      deferred.resolve(); //결과 보내기
    }
  );
}