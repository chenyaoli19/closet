import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class Header extends Component {
  render() {
    return (
      <div>
        <header>
		    <nav>
		      <ul>
		        <li><Link to='/'>Home</Link></li>
		        <li><Link to='/shuffle'>Shuffle</Link></li>
		        <li><Link to='/collage'>Collage</Link></li>
		      </ul>
		    </nav>
		  </header>
      </div>
    );
  }
}

export default Header;

