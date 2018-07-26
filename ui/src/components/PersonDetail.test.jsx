import { MemoryRouter } from 'react-router-dom';
import React from 'react';
import ReactDOM from 'react-dom';
import PersonDetail from './PersonDetail';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM
    .render(<MemoryRouter>
              <PersonDetail
                name="Levon Helm"
                description=""
                involved={[{}]}
              />
            </MemoryRouter>, div);
  ReactDOM.unmountComponentAtNode(div);
});
