if (Meteor.isClient) {


  Template.hello.greeting = function () {
    return "Welcome to Babble.";
  };

  Template.hello.events({
    'click input' : function () {
      // template data, if any, is available in 'this'
      if (typeof console !== 'undefined')
        console.log("You pressed the button");
	 console.log(Meteor.users.find().fetch()[0] )
    }
  });

 

}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
 console.log(Meteor.users.find().fetch() )
  });
}
