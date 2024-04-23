import React, { useState, useRef, useContext, useEffect } from "react";
import "./Test.css";
import { useNavigate } from "react-router-dom";
import AuthContext from "./Context/AuthContext";

function Cart() {
  const [expanded, setExpanded] = useState(true);

  const { booking, setBooking, total, setTotal } = useContext(AuthContext);
  const navigate = useNavigate();
  const expandedContainerRef = useRef();
  useEffect(() => {
    let totalPrice = 0;
    booking.map((product) => {
      totalPrice += product.data.price * product.quantity;
      return null;
    });
    setTotal(totalPrice);
  }, [booking, setTotal]);

  const incrementQuantity = (productId) => {
    const updatedBooking = [...booking];
    const productIndex = updatedBooking.findIndex(
      (product) => product.productId === productId
    );
    updatedBooking[productIndex].quantity = String(
      Number(updatedBooking[productIndex].quantity) + 1
    );
    setBooking(updatedBooking);
  };

  const decrementQuantity = (productId) => {
    const updatedBooking = [...booking];
    const productIndex = updatedBooking.findIndex(
      (p) => p.productId === productId
    );
    if (productIndex !== -1 && updatedBooking[productIndex].quantity > 1) {
      updatedBooking[productIndex].quantity -= 1;
      setBooking(updatedBooking);
    } else {
      updatedBooking.splice(productIndex, 1);
      setBooking(updatedBooking);
    }
  };
  const toggleExpand = () => {
    setExpanded(!expanded);
    setTimeout(() => {
      if (expandedContainerRef.current) {
        expandedContainerRef.current.scrollIntoView({
          behavior: "smooth",
          block: !expanded ? "start" : "end",
        });
      }
    }, 50);
  };

  return (
    <>
      <div
        className={`bottom-container ${expanded ? "expanded" : ""}`}
        ref={expandedContainerRef}
      >
        <div className="booking-details" onClick={toggleExpand}>
          <h4>Booking Details</h4>

          <h4>Total: AED {total}</h4>
        </div>

        <div className="scrollable-content">
          <div className="contentbar">
            <div className="row">
              {/* left cloumn: Cart */}
              <div className="col-lg-7">
                <div className="card m-b-30">
                  <div className="card-body">
                    <div className="cart-container">
                      <div className="cart-head">
                        <div className="table-responsive">
                          <table className="table table-borderless">
                            <thead>
                              <tr>
                                <th scope="col">Photo</th>
                                <th scope="col">Product</th>
                                <th scope="col">Qty</th>
                                <th scope="col">Price</th>
                                <th scope="col" className="text-right">
                                  Total
                                </th>
                              </tr>
                            </thead>
                            <tbody>
                              {booking.map((product, index) => (
                                <tr key={product.productId}>
                                  <td>
                                    <img
                                      src={product.data.image}
                                      className="img-fluid"
                                      width="35"
                                      alt="product"
                                    />
                                  </td>
                                  <td>{product.data.title}</td>
                                  <td>
                                    <div className="form-group mb-0 d-flex align-items-center">
                                      <button
                                        className="btn btn-sm btn-custom mr-1"
                                        onClick={() =>
                                          decrementQuantity(product.productId)
                                        }
                                      >
                                        -
                                      </button>
                                      <span className="p-2">
                                        {product.quantity}
                                      </span>
                                      <button
                                        className="btn btn-sm btn-custom ml-1"
                                        onClick={() =>
                                          incrementQuantity(product.productId)
                                        }
                                      >
                                        +
                                      </button>
                                    </div>
                                  </td>

                                  <td>{product.data.price}</td>
                                  <td className="text-right">
                                    {product.data.price * product.quantity}
                                  </td>
                                </tr>
                              ))}
                            </tbody>
                          </table>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              {/* right cloumn: Coupon and Subtotal */}
              <div className="col-lg-5">
                <div className="card m-b-30">
                  <div className="card-body">
                    <div className="order-note">
                      <form>
                        <div className="form-group">
                          <div className="input-group">
                            <input
                              type="search"
                              className="form-control"
                              placeholder="Coupon Code"
                              aria-label="Search"
                              aria-describedby="button-addonTags"
                            />
                            <div className="input-group-append">
                              <button
                                className="input-group-text"
                                type="submit"
                                id="button-addonTags"
                              >
                                Apply
                              </button>
                            </div>
                          </div>
                        </div>
                      </form>
                    </div>
                    <div className="order-total table-responsive">
                      <table className="table table-borderless text-right">
                        <tbody>
                          <tr>
                            <td>Sub Total :</td>
                            <td>AED {total}</td>
                          </tr>
                          <tr>
                            <td>Discount :</td>
                            <td>0%</td>
                          </tr>
                          <tr>
                            <td className="f-w-7 font-18">
                              <h4>Amount :</h4>
                            </td>
                            <td className="f-w-7 font-18">
                              <h4>AED {total}</h4>
                            </td>
                          </tr>
                        </tbody>
                      </table>{" "}
                      <div className="cart-footer text-center">
                        <button
                          className="make-payment"
                          onClick={() => navigate("/user")}
                        >
                          Make Payment
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default Cart;
