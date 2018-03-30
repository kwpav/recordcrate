import React, { Component } from 'react';
import AlbumCard from './AlbumCard';

function AlbumList(props) {
  return (
    <div className="record-collection container">
      <h1 className="page-title">{props.pageTitle}</h1>
      <div className="record-shelf card-deck">
        <AlbumCard albumName="The Last Waltz" bandName="The Band" />
        <AlbumCard albumName="The Last Waltz" bandName="The Band" />
        <AlbumCard albumName="The Last Waltz" bandName="The Band" />
      </div>
      <div className="record-shelf card-deck">
        <AlbumCard albumName="The Last Waltz" bandName="The Band" />
        <AlbumCard albumName="The Last Waltz" bandName="The Band" />
        <AlbumCard albumName="The Last Waltz" bandName="The Band" />
      </div>
    </div>
  );
}

export default AlbumList;
