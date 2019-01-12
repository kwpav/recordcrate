import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = props => (
  <nav className="sticky-top navbar navbar-expand-lg navbar-dark bg-dark">
    <Link className="navbar-brand" to="/">RecordCrate</Link>
    <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon" />
    </button>

    <div className="collapse navbar-collapse" id="navbarSupportedContent">
      <ul className="navbar-nav mr-auto">
        <li className="nav-item active">
          <Link className="nav-link" to="/collected">Collected<span className="sr-only">(current)</span></Link>
        </li>
        <li className="nav-item">
          <Link className="nav-link" to="/wanted">Wanted</Link>
        </li>
      </ul>
      <form className="form-inline mt-2 mt-lg-0">
        <input className="form-control mr-sm-2" type="search" placeholder="Dig through the crates..." aria-label="Search" />
        <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
      </form>
      <ul className="navbar-nav mr-right">
        <li className="nav-item">
          <Link className="nav-link" to="/signin">Sign in</Link>
        </li>
      </ul>
    </div>
  </nav>
);

export default Navbar;
