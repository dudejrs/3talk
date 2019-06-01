var express = require('express');
var router = express.Router();
var users = require('../users.json');

router.get('/', function (req, res, next) {
  res.send(users)
});

router.get('/:id', function (req, res, next) {
  var id = parseInt(req.params.id, 10)
  var	user = users.filter(function (user) {
    return user.id === id
  });
  res.send(user)
});

module.exports = router;