import React from 'react';
import {
  BrowserRouter as Router,
  Route,
  Switch,
} from 'react-router-dom';
import AlbumList from './AlbumList';

function Main() {
  return (
    <main>
      <Switch>
        <Route exact path="/" component={AlbumList} />
      </Switch>
    </main>
  );
}

export default Main;
