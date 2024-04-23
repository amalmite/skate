import React, { useContext } from 'react';
import './UserDetails.css'
import cardimg1 from '../../images/carousal1.jpg'
import { useNavigate } from 'react-router-dom';
import AuthContext from '../Context/AuthContext';


const UserDetails = () => {

    const navigate=useNavigate()
    const {userData,setUserData}=useContext(AuthContext)
    
      const handleChange = (e) => {
        const { name, value } = e.target;
        setUserData({
          ...userData,
          [name]: value,
        });
      };
    
      const handleSubmit = (e) => {
        e.preventDefault();
        navigate('/payment')
      }
    return (

        <div className='user-main' style={{ backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url(${cardimg1})` }}>
        <div className="form-container ">
          <p className="title">Personal Details</p>
          <form className="form" onSubmit={handleSubmit}>
            <input type="text" name="fullName" className="input" placeholder="Full Name" value={userData.fullName} onChange={handleChange} />
            <input type="email" name="email" className="input" placeholder="Email" value={userData.email} onChange={handleChange} />
            <input type="text" name="mobileNumber" className="input" placeholder="Mobile Number" value={userData.mobileNumber} onChange={handleChange} />
            <textarea name="address" className="input" placeholder="Address" value={userData.address} onChange={handleChange}></textarea>
            <button type="submit" className="form-btn" >Submit</button>
          </form>
        </div>
      </div>

    );
}

export default UserDetails;
