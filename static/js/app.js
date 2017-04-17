'use strict';   // See note about 'use strict'; below

var wbApp = angular.module('wbApp', [
 'ngRoute',
 'ui.bootstrap'
]);

wbApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/', {
                templateUrl: '/static/partials/index.html',
            }).
            when('/about', {
                templateUrl: '../static/partials/about.html',
                controller: 'AboutCtrl'
            }).
            when('/home', {
                templateUrl: '../templates/home.html',
                controller: 'HomeCtrl'
            }).
            otherwise({
                 redirectTo: '/'
            });
    }]);

wbApp.controller('AboutCtrl', ['$http','$scope',function($http,$scope) {

    $scope.loading = false;

    //$scope.callData = function($event){
    $scope.callData = function(){
        //$event.preventDefault();
        $scope.loading = true;
        $http({
            method:'GET',
            url:'/ml',
            headers: {
               'Content-Type': 'application/json;charset=utf-8'
            }
        })
        .then(function(resp){
            $scope.results = resp.data;
        },function(error){
            console.log(error);
        }).finally(function() {
            $scope.loading = false;
        });
    }
}]);

wbApp.controller('NavbarCtrl', function($scope) {
  $scope.isCollapsed = true;
});