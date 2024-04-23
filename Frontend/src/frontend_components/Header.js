import React, { useContext, useState } from 'react';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import logo from '../images/logo.png';
import './Header.css';
import { useNavigate } from 'react-router-dom';
import AuthContext from '../components/Context/AuthContext';

const Header = () => {
  const [expanded, setExpanded] = useState(false); // This state controls the collapse
  const navigate = useNavigate();
  const {logout}=useContext(AuthContext)

  // This function is used for navigation and closing the collapse
  const navigateAndCollapse = (path) => {
    navigate(path);
    setExpanded(false); // This will close the navbar after navigation
  };



  return (
<Navbar expand="lg" className="bg-black text-white p-0 m-auto fixed-top" style={{ boxShadow: '0px 2px 5px rgba(0, 0, 0, 0.1)', height: '80px' }} expanded={expanded}>
  <Container>
    <Navbar.Brand href="/">
      <img
        alt="Company logo"
        src={logo}
        width="100"
        height="70"
        className="d-inline-block align-top" 
        />
        <Navbar.Brand className="fw-bold fs-2 text-danger d-none">SKATE GATE </Navbar.Brand>
    </Navbar.Brand>
    <Navbar.Toggle aria-controls="basic-navbar-nav" style={{ backgroundColor: 'white', borderColor: 'red' }}
              onClick={() => setExpanded(expanded ? false : "expanded")} 
              />
    <Navbar.Collapse id="basic-navbar-nav" style={{backgroundColor:'#0a0a0a'}}>
      <Nav className="w-100 justify-content-center">
        <Nav.Link onClick={() => navigateAndCollapse('/')} className='px-4 text-white nav-link-hover d-flex align-items-center justify-content-center'>Home</Nav.Link>
        <Nav.Link onClick={() => navigateAndCollapse('/about')}className='px-4 text-white nav-link-hover d-flex align-items-center justify-content-center'>About</Nav.Link>
        <Nav.Link onClick={() => navigateAndCollapse('/contact')} className='px-4 text-white nav-link-hover d-flex align-items-center justify-content-center'>Contact</Nav.Link>
        {localStorage.getItem('tokens')?
        <Nav.Link onClick={() => logout()} className='px-4 text-white nav-link-hover d-flex align-items-center justify-content-center'>Logout</Nav.Link>:
        ''
        }
        
      </Nav>
    </Navbar.Collapse>
  </Container>
</Navbar>


  );
};

export default Header;
