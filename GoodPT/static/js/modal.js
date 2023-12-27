
(function() {
    'use strict';
  
    var app = angular.module('app', ['ngDialog']);
  
    // ngDialog config
    app.config(['ngDialogProvider', function(ngDialogProvider) {
      ngDialogProvider.setDefaults({
        className: 'modal',
        plain: false,
        showClose: false,
        closeByDocument: true,
        closeByEscape: true,
        appendTo: false
      });
    }]);
  
    // view controller
    app.controller("ModalDemoCtrl", function(ngDialog) {
      var vm = this;
  
      vm.clickToOpen = function() {
        var dialog = ngDialog.open({
          template: 'templateId',
          controller: "ModalCtrl",
          controllerAs: 'modal',
          resolve: {
            injected: () => {
              return {
                propertyInjection: '약관 내용 ~~~~~~'
              }
            }
          },
        });
        
        dialog.closePromise.then(function (data) {
          console.log('Returned data:');
          console.log(data);
          if(data.value === 'submit') {
            console.log('You clicked submit!');
          }
        });;
      };
    });
  
    // modal controller
    app.controller("ModalCtrl", function($scope, ngDialog, injected) {
      console.log('Modal opened!');
      var ngDialogId = $scope.ngDialogId;
      var vm = this;
  
      vm.headingText = "Heading";
      vm.injected = injected;
      vm.close = function(data) {
        ngDialog.close(ngDialogId, data);
      }
    });
  })();