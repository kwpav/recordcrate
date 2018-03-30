import React, { Component } from 'react';
import { Link } from 'react-router-dom';

function BandDetail(props) {
  return (
    <div className="record-collection container">

      <div>
        <h1 id="page-title">The Band</h1>
        <img src="https://img.discogs.com/bHGI7q-dbvdhlIbEmVhguF_KIFw=/fit-in/455x455/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-1564673-1443567983-5247.jpeg.jpg" />
      </div>

      <div id="page-details">
        <p>
          The Band was a Canadian-American roots rock group formed in Toronto, Ontario in 1968 by Rick Danko (bass guitar, vocals), Garth Hudson (keyboards, saxophone), Richard Manuel (keyboards, vocals), Robbie Robertson (guitar, vocals), and Levon Helm (drums, vocals). The members of The Band first came together as rockabilly singer Ronnie Hawkins's backing group, the Hawks, which they joined one by one between 1958 and 1963.
          </p>

        <p>
          In 1964, they separated from Hawkins, after which they toured and released a few singles as Levon and the Hawks and the Canadian Squires. The next year, Bob Dylan hired them for his U.S. tour in 1965 and world tour in 1966.[1] Following the 1966 tour, the group moved with Dylan to Saugerties, New York, where they made the informal 1967 recordings that became The Basement Tapes, the basis for their 1968 debut album, Music from Big Pink. Because they were always "the band" to various frontmen, Helm said the name "The Band" worked well when the group came into its own.[2][a] The group began performing as The Band in 1968 and went on to release ten studio albums. Dylan continued to collaborate with The Band over the course of their career, including a joint 1974 tour.
        </p>
      </div>

      <div id="members">
        <h3>Members</h3>
        <a href="#">Rick Danko</a>, <a href="#">Levon Helm</a>, <a href="#">Garth Hudson</a>, <a href="#">Richard Manuel</a>
      </div>

      <div id="discography">
        <h3>Discography</h3>
        <table className="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Label</th>
              <th scope="col">Year</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row"><Link to="/album/1">The Last Waltz</Link></th>
              <td>Warner Bros. Records</td>
              <td>1978</td>
            </tr>
            <tr>
              <th scope="row"><Link to="/album/1">The Last Waltz</Link></th>
              <td>Warner Bros. Records</td>
              <td>1978</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default BandDetail;
