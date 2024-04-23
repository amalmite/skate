import React from 'react'


const ExampleCarouselImage = ({ src }) => {
  
  return (
      <div  className='mw-100 overflow-hidden' style={{maxHeight:'70vh'}}>
        <img src={src} alt="carousal"  className='w-100 h-100 object-fit-cover' fluid />
      </div>
  )
}

export default ExampleCarouselImage
