import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import HomePage from './components/Home/HomePage';
import Details from './components/Details';
import AfterPayment from './components/Payment/AfterPayment';
import Header from './frontend_components/Header';
import Footer from './frontend_components/Footer';
import UserDetails from './components/UserDetails/UserDetails';
import About from './components/About/About';
import Contact from './components/Contact/Contact';
import Login from './components/Auth/Login';
import Register from './components/Auth/Register';
import { AuthProvider } from './components/Context/AuthContext';
import Otp from './components/Auth/Otp';
import Forgotpassword from './components/Auth/Forgotpassword';
import Resetpassword from './components/Auth/Resetpassword';
import UserProfile from './components/Profile/UserProfile';


const MainLayout = ({ children }) => (
  <>
    <Header />
    <div style={{ paddingTop: '80px' }}>
      {children}
    </div>
    <Footer />
  </>
);


function App() {
  


  return (

    <div>
      <Router>
      <AuthProvider>
        <Routes>
          <Route path="/" element={<MainLayout><HomePage /></MainLayout>} />
          <Route path="/details/:id" element={<MainLayout><Details /></MainLayout>} />
          <Route path="/user" element={<MainLayout><UserDetails /></MainLayout>} />
          <Route path="/payment" element={<MainLayout><AfterPayment /></MainLayout>} />
          <Route path='/about' element={<MainLayout><About/></MainLayout>}/>
          
          <Route path='/contact' element={<MainLayout><Contact/></MainLayout>}/>
          <Route path='/profile' element={<MainLayout><UserProfile/></MainLayout>}/>

          
          
          <Route path="/login" element={<Login />} />
          <Route path="/otp" element={<Otp />} />
          <Route path="/forgotpassword" element={<Forgotpassword />} />
          <Route path="/reset-password/:uidb64/:token"  element={<Resetpassword />} />
          <Route path="/register" element={<Register />} />

        </Routes>
        </AuthProvider>
      </Router>
    </div>
  );
}

export default App;
