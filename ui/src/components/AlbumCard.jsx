import React from 'react';
import { Link } from 'react-router-dom';

function AlbumCard(props) {
  return (
    <div className="record-info card">
      <a href="#"><img className="card-img-top" src="http://placehold.it/225" alt="Card image cap" /></a>
      <div className="card-body">
        <Link to="/album/1"><h4 className="album-name card-title">{props.albumName}</h4></Link>
        <Link to="/band/1"><h6 className="artist-name card-subtitle mb-2 text-muted">{props.bandName}</h6></Link>
        <p className="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
        <a href="#" className="collect-link card-link text-muted disabled">Collected</a>
      </div>
    </div>
  );
}

export default AlbumCard;
