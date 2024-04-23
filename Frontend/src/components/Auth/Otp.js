
import React, { useState } from 'react';
import './Otp.css';
import { useNavigate } from 'react-router-dom';
import axiosInstance from '../utils/axiosIntance';
import { ToastContainer,toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const Otp = () => {
  const [otp, setOtp] = useState({
    otp1: '',
    otp2: '',
    otp3: '',
    otp4: '',
    otp5: '',
    otp6: ''
  });

  const navigate = useNavigate();

  const handleChange = (value, event) => {
    setOtp({ ...otp, [value]: event.target.value });
  };
  
  const inputfocus = (event) => {
    if (event.key === 'Delete' || event.key === 'Backspace') {
      const next = event.target.tabIndex - 2;
      if (next > -1) {
        event.target.form.elements[next].focus();
      }
    } else {
      const next = event.target.tabIndex;
      if (next < 6) {
        event.target.form.elements[next].focus();
      }
    }
  };
  
  const handleSubmit = async (event) => {
    event.preventDefault();
    const otpValue = Object.values(otp).join('');
    console.log(otpValue);

    try {
      const response = await axiosInstance.post('/api/activation/', {
        code: otpValue, 
      });
      if(response.status === 200){
        toast.success('Otp verification completed ')
        navigate('/login')
      }


    } catch (error) {
        if(error.response.status ===400){
            toast.error('Invalid confirmation code ')
        }
        console.error('Error during OTP verification:', error);
    }
  };




  return (
    <div className='otp-main'>
      <ToastContainer />

      <form className="form" onSubmit={handleSubmit}>
        <div className="info">
          <h2>OTP VERIFICATION</h2>
          <p className="description">Please enter the code we have sent you.</p>
        </div>

        <div className="inputs">
        {Array.from({ length: 6 }, (_, index) => (
          <input
            key={index}
            name={`otp${index + 1}`}
            type="text"
            autoComplete="off"
            className="otpInput"
            value={otp[`otp${index + 1}`]}
            onChange={(e) => handleChange(`otp${index + 1}`, e)}
            tabIndex={index + 1}
            maxLength="1"
            onKeyUp={inputfocus}
          />
        ))}
        </div>
        <button className='validate'>Submit</button>
      </form>
    </div>
  );
};

export default Otp;
