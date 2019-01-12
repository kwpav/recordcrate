import React from 'react';

const SignIn = props => (
  <div className="text-center">
    <form className="form-signin">
      <h1 className="page-title">Please sign in</h1>
      <label htmlFor="inputEmail" className="sr-only">Email address</label>
<input type="email" id="inputEmail" className="form-control" placeholder="Email address" required />
      <label htmlFor="inputPassword" className="sr-only">Password</label>
      <input type="password" id="inputPassword" className="form-control" placeholder="Password" required />
      <div className="checkbox mb-3">
        <label>
          <input type="checkbox" value="remember-me" /> Remember me
        </label>
      </div>
      <button className="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
    </form>
  </div>
);

export default SignIn;
