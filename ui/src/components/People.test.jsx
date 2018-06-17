import { MemoryRouter } from 'react-router-dom';
import React from 'react';
import ReactDOM from 'react-dom';
import People from './People';


it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM
    .render(<MemoryRouter>
              <People
                header="Members"
                people={
                  ['Rick Danko',
                  'Levon Helm',
                  'Garth Hudson',
                  'Richard Manual']
                }
              />
            </MemoryRouter>, div);
  ReactDOM.unmountComponentAtNode(div);
});
