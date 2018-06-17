import { MemoryRouter } from 'react-router-dom';
import React from 'react';
import ReactDOM from 'react-dom';
import AlbumList from './AlbumList';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM
    .render(<MemoryRouter>
              <AlbumList />
            </MemoryRouter>, div);
  ReactDOM.unmountComponentAtNode(div);
});
