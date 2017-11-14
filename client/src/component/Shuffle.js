import axios from 'axios';
import React, { Component } from 'react';

class Shuffle extends Component {

	constructor(props) {
	    super(props);

	    const iniState = {
	      tops: [],
	      bottoms: [],
	      alls: []
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
  				const initializeData = {
  					tops: topsRes.data,
  					bottoms: bottomsRes.data,
  					alls: allsRes.data
  				};
  				this.setState(initializeData)
  			}));
  	}

	onShuffle() {
		console.log("clicked!!")
	}

	fetchItemsWithParam(bottom_top) {
	    const url = 'http://localhost:5000/item/bottom_top/' + bottom_top;
	    return axios.get(url);
	}

	render() {
		return (
		  <div>
		    <h1>Shuffle</h1>
		    <button onClick={this.onShuffle}>
			  Shuffle Clothes
			</button>
		  </div>
		);
	}
}

export default Shuffle;

