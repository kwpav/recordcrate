import { MemoryRouter } from 'react-router-dom';
import React from 'react';
import ReactDOM from 'react-dom';
import AlbumDetail from './AlbumDetail';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<MemoryRouter>
                    <AlbumDetail />
                  </MemoryRouter>, div);
  ReactDOM.unmountComponentAtNode(div);
});
