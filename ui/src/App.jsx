import React from 'react';
import {
  BrowserRouter as Router,
  Route,
} from 'react-router-dom';
import Navbar from './components/Navbar';
import AlbumList from './components/AlbumList';
import AlbumDetail from './components/AlbumDetail';
import BandDetail from './components/BandDetail';
import PersonDetail from './components/PersonDetail';
import SignIn from './components/SignIn';
import './App.css';

const App = () => (
  <Router>
    <div>
      <Navbar />
      <Route
        exact={true}
        path="/"
        component={AlbumList}
      />
      <Route
        path="/collected"
        render={() => (<AlbumList pageTitle="Collected" />)}
      />
      <Route
        path="/wanted"
        render={() => (<AlbumList pageTitle="Wanted" />)}
      />
      <Route
        path="/album/:id"
        render={() =>
          (<AlbumDetail
            albumName="The Last Waltz"
            bandName="The Band"
            tracks={
              [
                { id: 1, title: 'Theme from the Last Waltz', length: '3:28' },
                { id: 2, title: 'Up on Cripple Creek', length: '4:44' },
              ]
            }
            people={
              [
                { id: 1, name: 'Rick Danko' },
                { id: 2, name: 'Levon Helm' },
                { id: 3, name: 'Garth Hudson' },
                { id: 4, name: 'Richard Manual' },
              ]
            }
          />)}
      />
      <Route
        path="/band/:id"
        component={BandDetail}
      />
      <Route
        path="/person/:id"
        component={PersonDetail}
      />
      <Route
        path="/signin"
        component={SignIn}
      />
    </div>
  </Router>
);

export default App;
