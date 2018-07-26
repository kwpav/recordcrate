import React from 'react';
import {
  BrowserRouter as Router,
  Route,
} from 'react-router-dom';
import PropTypes from 'prop-types';
import Navbar from './components/Navbar';
import AlbumList from './components/AlbumList';
import AlbumDetailContainer from './components/AlbumDetailContainer';
import BandDetailContainer from './components/BandDetailContainer';
import PersonDetailContainer from './components/PersonDetailContainer';
import SignIn from './components/SignIn';
import './App.css';

const App = ({ records }) => (
  <Router>
    <div>
      <Navbar />
      <Route
        exact={true}
        path="/"
        render={() => <AlbumList records={[records]} />}
      />
      <Route
        path="/collected"
        render={() => <AlbumList pageTitle="Collected" records={[records]} />}
      />
      <Route
        path="/wanted"
        render={() => (<AlbumList pageTitle="Wanted" records={[records]} />)}
      />
      <Route
        path="/albums/:id"
        component={AlbumDetailContainer}
      />
      <Route
        path="/bands/:id"
        component={BandDetailContainer}
      />
      <Route
        path="/people/:id"
        component={PersonDetailContainer}
      />
      <Route
        path="/signin"
        component={SignIn}
      />
    </div>
  </Router>
);

App.propTypes = {
  records: PropTypes.arrayOf(PropTypes.object).isRequired,
};

export default App;
