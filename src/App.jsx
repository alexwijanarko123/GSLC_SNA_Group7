import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Tugas GSLC DevOps - Kelompok 7 </h1>
      <h1>Alexander Bagus Wijanarko - 2802407824 </h1>
      <h1>Kyoshiro Kaynelie - 2802407553</h1>
      <h1>Mikhael Filemon - 2802471221</h1>
    </>
  )
}

export default App
