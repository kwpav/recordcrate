import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route,
} from 'react-router-dom';
import Navbar from './components/Navbar';
import AlbumList from './components/AlbumList';
import AlbumDetail from './components/AlbumDetail';
import BandDetail from './components/BandDetail';
import './App.css';

class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <Navbar />
          <Route exact={true} path="/" component={AlbumList} />
          <Route path="/collected"
                 render = {() => (<AlbumList pageTitle="Collected" />)} />
          <Route path="/wanted"
                 render = {() => (<AlbumList pageTitle="Wanted" />)} />
          <Route path="/album/:id" component={AlbumDetail} />
          <Route path="/band/:id" component={BandDetail} />
        </div>
      </Router>
    );
  }
}

export default App;
