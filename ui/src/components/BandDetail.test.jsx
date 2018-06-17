import { MemoryRouter } from 'react-router-dom';
import React from 'react';
import ReactDOM from 'react-dom';
import BandDetail from './BandDetail';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM
    .render(<MemoryRouter>
              <BandDetail />
            </MemoryRouter>, div);
  ReactDOM.unmountComponentAtNode(div);
});
