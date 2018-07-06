import React from 'react';
import ReactDOM from 'react-dom';
import CollectWantLinks from './CollectWantLinks';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM
    .render(<CollectWantLinks status="" />, div);
  ReactDOM.unmountComponentAtNode(div);
});
