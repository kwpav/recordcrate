import { MemoryRouter } from 'react-router-dom';
import React from 'react';
import ReactDOM from 'react-dom';
import AlbumDetail from './AlbumDetail';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<MemoryRouter>
                    <AlbumDetail
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
                  />
                  </MemoryRouter>, div);
  ReactDOM.unmountComponentAtNode(div);
});
