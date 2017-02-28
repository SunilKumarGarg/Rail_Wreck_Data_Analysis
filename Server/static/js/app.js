(function(){
var app = angular.module('RailWreck',['ngRoute']);

app.config(function($routeProvider){
  $routeProvider

  .when('/Home',{
    templateUrl : "/static/Home.html",
    controller : 'DataController'
  })
  
  .when('/State',{
    templateUrl : '/static/state.html',
    controller : 'DataController'
  })

  .when('/Railroad',{
    templateUrl : '/static/Railroad.html',
    controller : 'DataController'
  }) 

  .when('/Hour',{
    templateUrl : '/static/hour.html',
    controller : 'DataController'
  })

  .when('/Year',{
    templateUrl : '/static/Year.html',
    controller : 'DataController'
  })

  .when('/Month',{
    templateUrl : '/static/Month.html',
    controller : 'DataController'
  })

  .when('/Date',{
    templateUrl : '/static/Date.html',
    controller : 'DataController'
  })

  .when('/City',{
    templateUrl : '/static/City.html',
    controller : 'DataController'
  })

  .otherwise({redirectTo: '/'})
});

app.controller("DataController", function($scope, Service , $timeout){

  $scope.RailWreckCityData=[];
  $scope.RailWreckStateData=[];
  $scope.RailWreckHourData=[];
  $scope.RailWreckRailroadData=[];

  $scope.RailWreckYearData=[];
  $scope.RailWreckMonthData=[];
  $scope.RailWreckDateData=[];

  $scope.$watch( Service.RailWreckCityData, function ( ) 
  {
      $scope.RailWreckCityData = Service.returnRailWreckCityData();
      console.log("This is me:" + $scope.RailWreckCityData)
  });
  $scope.$watch( Service.RailWreckStateData, function ( ) 
  {
      $scope.RailWreckStateData = Service.returnRailWreckStateData();
      console.log("This is me:" + $scope.RailWreckStateData)
  });
  $scope.$watch( Service.RailWreckHourData, function ( ) 
  {
      $scope.RailWreckHourData = Service.returnRailWreckHourData();
      console.log("This is me:" + $scope.RailWreckHourData)
  });
  $scope.$watch( Service.RailWreckRailroadData, function ( ) 
  {
      $scope.RailWreckRailroadData = Service.returnRailWreckRailroadData();
      console.log("This is me:" + $scope.RailWreckRailroadData)
  });

  $scope.$watch( Service.RailWreckYearData, function ( ) 
  {
      $scope.RailWreckYearData = Service.returnRailWreckYearData();
      console.log("This is me:" + $scope.RailWreckYearData)
  });

  $scope.$watch( Service.RailWreckMonthData, function ( ) 
  {
      $scope.RailWreckMonthData = Service.returnRailWreckMonthData();
      console.log("This is me:" + $scope.RailWreckMonthData)
  });

  $scope.$watch( Service.RailWreckDateData, function ( ) 
  {
      $scope.RailWreckDateData = Service.returnRailWreckDateData();
      console.log("This is me:" + $scope.RailWreckDateData)
  });

 $scope.getRailWreckCityData = function()
 {
 	Service.getRailWreckCityData();
 }
 $scope.getRailWreckStateData = function()
 {
 	Service.getRailWreckStateData();
 }
 $scope.getRailWreckHourData = function()
 {
 	Service.getRailWreckHourData();
 }
 $scope.getRailWreckRailroadData = function()
 {
 	Service.getRailWreckRailroadData();
 }
 $scope.getRailWreckYearData = function()
 {
 	Service.getRailWreckYearData();
 }
 $scope.getRailWreckMonthData = function()
 {
 	Service.getRailWreckMonthData();
 }
 $scope.getRailWreckDateData = function()
 {
 	Service.getRailWreckDateData();
 }

});

app.factory( 'Service', function($http) { 

  var RailWreckCityData=[];
  var RailWreckStateData=[];
  var RailWreckHourData=[];
  var RailWreckRailroadData=[];

  var RailWreckYearData=[];
  var RailWreckMonthData=[];
  var RailWreckDateData=[];

  

  return {

      getRailWreckCityData: function()
        {
          $http.get("http://127.0.0.1:5000/RailAccident/City").then(function successCallback(response) 
          {            
            // RailWreckStateData = JSON.stringify(response.data);
            RailWreckCityData = response.data;
            
            }, function successCallback(response) 
            {
              alert("Server has some problem. Please try after sometime.");
            })
        },

        returnRailWreckCityData:function()
        {
          return RailWreckCityData;
        },

       getRailWreckStateData: function()
        {
          $http.get("http://127.0.0.1:5000/RailAccident/State").then(function successCallback(response) 
          {            
            // RailWreckStateData = JSON.stringify(response.data);
            RailWreckStateData = response.data;
            
            }, function successCallback(response) 
            {
              alert("Server has some problem. Please try after sometime.");
            })
        },

        returnRailWreckStateData:function()
        {
          return RailWreckStateData;
        },


        getRailWreckHourData: function()
        {
          $http.get("http://127.0.0.1:5000/RailAccident/Hour").then(function successCallback(response) 
          {            
           // RailWreckHourData = JSON.stringify(response.data);
            RailWreckHourData = response.data;
            
            }, function successCallback(response) 
            {
              alert("Server has some problem. Please try after sometime.");
            })
        },

        returnRailWreckHourData:function()
        {
          return RailWreckHourData;
        },





        getRailWreckRailroadData: function()
        {
          $http.get("http://127.0.0.1:5000/RailAccident/Railroad").then(function successCallback(response) 
          {            
            // RailWreckStateData = JSON.stringify(response.data);
            RailWreckRailroadData = response.data;
            
            }, function successCallback(response) 
            {
              alert("Server has some problem. Please try after sometime.");
            })
        },

        returnRailWreckRailroadData:function()
        {
          return RailWreckRailroadData;
        },



        getRailWreckYearData: function()
        {
          $http.get("http://127.0.0.1:5000/RailAccident/Year").then(function successCallback(response) 
          {            
           // RailWreckHourData = JSON.stringify(response.data);
            RailWreckYearData = response.data;
            
            }, function successCallback(response) 
            {
              alert("Server has some problem. Please try after sometime.");
            })
        },

        returnRailWreckYearData:function()
        {
          return RailWreckYearData;
        },

        getRailWreckMonthData: function()
        {
          $http.get("http://127.0.0.1:5000/RailAccident/Month").then(function successCallback(response) 
          {            
           // RailWreckHourData = JSON.stringify(response.data);
            RailWreckMonthData = response.data;
            
            }, function successCallback(response) 
            {
              alert("Server has some problem. Please try after sometime.");
            })
        },

        returnRailWreckMonthData:function()
        {
          return RailWreckMonthData;
        },

        getRailWreckDateData: function()
        {
          $http.get("http://127.0.0.1:5000/RailAccident/Date").then(function successCallback(response) 
          {            
           // RailWreckHourData = JSON.stringify(response.data);
            RailWreckDateData = response.data;
            
            }, function successCallback(response) 
            {
              alert("Server has some problem. Please try after sometime.");
            })
        },

        returnRailWreckDateData:function()
        {
          return RailWreckDateData;
        },
      
      };
});

})();