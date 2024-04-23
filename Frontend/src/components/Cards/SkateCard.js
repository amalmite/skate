import React from 'react'
import Card from 'react-bootstrap/Card';
import './SkateCard.css'
import { useNavigate } from 'react-router-dom';

 
const SkateCard = ({image,skate,price,clr,id}) => {
    const navigate=useNavigate()
    return (
        <>

        {/* Skate card (65,55) */}
            <Card style={{borderRadius:'0px', border:'0px' }} onClick={()=>navigate(`details/${id}`)}>
                <Card.Img variant="top" height={375} src={image} className='object-fit-cover w-100' alt='Skate'/>
                <Card.Footer className='skate-footer' style={{ backgroundColor: clr,color:'white', borderRadius:'0px', border:'0px' }}>
                    <div className='skate-hover'>{skate} </div> 
                    <div className='skate-hover'>AED {price}</div>
                </Card.Footer>
            </Card>

        </>
    )
}

export default SkateCard
