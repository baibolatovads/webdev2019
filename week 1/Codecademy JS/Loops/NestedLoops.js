// Write your code below
const bobsFollowers = ['Dariya', 'Shynar', 'Dan', 'Ars'];

const tinasFollowers = ['Dariya', 'Nina', 'Dan'];

const mutualFollowers = [];

for(let i = 0; i < bobsFollowers.length; i++){
  for(let j = 0; j < tinasFollowers.length; j++){
    if(bobsFollowers[i] === tinasFollowers[j]){
      mutualFollowers.push(bobsFollowers[i]);
    }
  }
}