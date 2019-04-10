const agent = require('superagent');

const res = agent
.get('https://maps.googleapis.com/maps/api/geocode/json?address=Lucknow&key=AIzaSyC2kABM-JOsk7pG8oUHz8CoiTEEFqupaFo')
.then(res => {
    lat = res.body.results[0].geometry.location.lat;
    lng = res.body.results[0].geometry.location.lng;

    return ({"lat": lat, "lng": lng});
})
.then( res => {
    agent.get(`https://maps.googleapis.com/maps/api/timezone/json?location=${res.lat},${res.lng}&timestamp=1458000000&key=AIzaSyC2kABM-JOsk7pG8oUHz8CoiTEEFqupaFo`)
    .then(res =>{
        console.log(res);
    })
    .catch(err => {
        console.log(err);
    })
})
.catch((err) =>{

    console.log(err);
})

