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
                  [
                    { id: 1, name: 'Rick Danko' },
                    { id: 2, name: 'Levon Helm' },
                    { id: 3, name: 'Garth Hudson' },
                    { id: 4, name: 'Richard Manual' },
                  ]
                }
              />
            </MemoryRouter>, div);
  ReactDOM.unmountComponentAtNode(div);
});
