import React from 'react';
import AlbumTable from './AlbumTable';

function PersonDetail(props) {
  return (
    <div className="container">
      <div>
        <h1 className="page-title">Levon Helm</h1>
        <img src="http://placehold.it/225" alt="Levon Helm" />
      </div>

      <div id="page-details">
        <p>Mark Lavon "Levon" Helm (May 26, 1940 – April 19, 2012)[1] was an American musician and actor who achieved fame as the drummer and one of the vocalists for The Band. Helm was known for his deeply soulful, country-accented voice, multi-instrumental ability, and creative drumming style, highlighted on many of the Band's recordings, such as "The Weight", "Up on Cripple Creek", and "The Night They Drove Old Dixie Down".</p>
      </div>

      <AlbumTable
        header="Involved"
        headers={['Title', 'Record Label', 'Country', 'Year']}
        albums={[{
            name: 'The Last Waltz',
            recordLabel: 'Warner Bros.',
            country: 'US',
            releaseDate: '1978',
          }]}
      />
    </div>
  );
}

export default PersonDetail;
