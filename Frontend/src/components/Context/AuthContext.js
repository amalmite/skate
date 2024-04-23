import { createContext, useState } from "react";
import { jwtDecode } from "jwt-decode";
  import { useNavigate } from "react-router-dom";
import axiosInstance from "../utils/axiosIntance";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
const AuthContext = createContext();

export default AuthContext;

export const AuthProvider = ({ children }) => {
  const navigate = useNavigate();

  const [token, setToken] = useState(
    localStorage.getItem("token")
      ? JSON.parse(localStorage.getItem("token"))
      : null
  );
  const [user, setUser] = useState(
    localStorage.getItem("token")
      ? jwtDecode(localStorage.getItem("token"))
      : null
  );
  const [loading, setLoading] = useState(false);



  const login = async (e) => {
    e.preventDefault();
    try {
      const response = await axiosInstance.post("api/login/", {
        // const response = await axios.post('http://127.0.0.1:8000/api/employees-login/', {
       
            username: e.target.username.value,
            password: e.target.password.value
          
        });
        console.log(response.data);
      if (response.status === 200) {
        const data = response.data;
        setToken(data.tokens);
        localStorage.setItem("tokens", JSON.stringify(data.tokens));
        toast.success('Login successfully', {
          onClose: () => {
            navigate('/');
          }
        });
  
      }
    } catch (error) {
      console.error("Error during login:", error);
      if (error.response) {
        const statusCode = error.response.status;
        if (statusCode === 400) {
          Object.entries(error.response.data).forEach(([key, value]) =>
            toast.error(`${key}: ${value[0]}`)
          );
        } else if (statusCode === 401) {
          toast.error(error.response.data.detail);
        } else {
          toast.error("An unexpected error occurred. Please try again.");
        }
      } else {
        toast.error("An unexpected error occurred. Please try again.");
      }
    }
  };


const logout = () => {
    setToken(null);
    setUser(null);
    localStorage.removeItem('tokens');
    navigate('/login');
};


  const [booking, setBooking] = useState([]);
  const [total, setTotal] = useState(0);
  const [userData, setUserData] = useState({
    fullName: "",
    email: "",
    mobileNumber: "",
    address: "",
  });

  const contextData = {
    booking: booking,
    total: total,
    setBooking: setBooking,
    setTotal: setTotal,
    userData: userData,
    setUserData: setUserData,
    login: login,
    logout:logout,
  };

  return (
    <AuthContext.Provider value={contextData}>
      {loading ? null : children}
    </AuthContext.Provider>
  );
};
