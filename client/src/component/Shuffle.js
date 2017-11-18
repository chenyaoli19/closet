import axios from 'axios';
import React, { Component } from 'react';

class Shuffle extends Component {

	constructor(props) {
	    super(props);

	    const iniState = {
	    	loaded: false,
		    imageSection: null
	    };

	    this.state = iniState;
	    this.onShuffle = this.onShuffle.bind(this);
  	}

  	componentDidMount() {
  		axios.all([
  			this.fetchItemsWithParam('top'),
  			this.fetchItemsWithParam('bottom'),
  			this.fetchItemsWithParam('all')
  			]).then(axios.spread((topsRes, bottomsRes, allsRes) => {
  				var tops = topsRes.data.data,
					bottoms = bottomsRes.data.data,
					alls = allsRes.data.data;

				var topImageUrl = this.generateRandomTop(tops)["image_url"],
					bottomImageUrl = this.generateRandomBottomOrAll(bottoms, alls)["image_url"];

				var imageSection = function() {
					return (
						<div>
							<img src={topImageUrl}/>
		    				<img src={bottomImageUrl}/>	
						</div>
						)
				};

  				const initializeData = {
  					loaded: true,
  					imageSection: imageSection
  				};
  				this.setState(initializeData) 				
  			}));
  	}

	onShuffle() {
		console.log("clicked!!")
	}

	generateRandomTop(tops) {
		var len = tops.length,
		    rand_idx = Math.floor(Math.random()*(len));
		return tops[rand_idx]
	}

	generateRandomBottomOrAll(bottoms, alls) {
		var bottoms_len = bottoms.length,
			alls_len = alls.length,
			rand_idx = Math.floor(Math.random()*(bottoms_len+alls_len));
		if(rand_idx<=bottoms_len){
			return bottoms[rand_idx]
		}else{
			return alls[rand_idx-bottoms_len]
		}
	}

	fetchItemsWithParam(bottom_top) {
	    const url = 'http://localhost:5000/item/bottom_top/' + bottom_top;
	    return axios.get(url);
	}



	render() {
		return (
		  <div>
		    <h1>Shuffle</h1>
		  	{this.state.loaded}
		    <button onClick={this.onShuffle}>
			  Shuffle Clothes
			</button>
		  </div>
		);
	}
}

export default Shuffle;

