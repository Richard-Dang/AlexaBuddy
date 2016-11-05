/*
 * Add the following line to use the grade function:
 *    var messageGrader = require("<path_to_file>/test.js");
 */

var indico = require('indico.io');
indico.apiKey =  'f813d87aeb7c1fec9b38a95f466c414f';

var total;
var message;

//call this funtion to determine whether or not to say a message out loud
function grade(input){
  total = 0;
  message = input;
  indico.emotion(message).then(parseEmotion);
}

//used for calculating weighted average
function parseSentiment(res) {
  console.log(res);
  total += (0.31 * res);
  determineGrade();
}

//used for calculating weighted average
function parseEmotion(res){
  console.log(res);
  total += (0.26 * (1 - res.anger))
         + (0.26 * (1 - res.sadness))
         + (0.07 * (1 - res.fear))
         + (0.10 * (1 - res.surprise));
  indico.sentiment(message).then(parseSentiment);
}

function determineGrade(){
  if (total > 0.5666666){
    return true;
  } else {
    return false;
  }
}

//only the grade function should be accessible by other files
exports.grade = grade;
