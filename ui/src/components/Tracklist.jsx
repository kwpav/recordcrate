import React from 'react';

function Tracklist(props) {
  return (
    <div id="tracklist">
      <h3>Tracklist</h3>
      <table className="table table-hover">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Title</th>
            <th scope="col">Length</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">1.</th>
            <td>Theme from the Last Waltz</td>
            <td>3:28</td>
          </tr>
          <tr>
            <th scope="row">2.</th>
            <td>Up On Cripple Creek</td>
            <td>4:44</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default Tracklist;
