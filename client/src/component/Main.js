import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom'
import Home from './Home'
import Shuffle from './Shuffle'
import Collage from './Collage'

class Main extends Component {
  render() {
    return (
      <div>
        <main>
		  <Switch>
		    <Route exact path='/' component={Home}/>
		    <Route path='/shuffle' component={Shuffle}/>
		    <Route path='/collage' component={Collage}/>
		  </Switch>
		</main>
      </div>
    );
  }
}

export default Main;

