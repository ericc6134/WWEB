console.log('hello');

function fn1() {

var notification = webkitNotifications.createNotification(

  'Hello!',  // notification title
  'Lorem ipsum...'  // notification body text
);

notification.show();

};
