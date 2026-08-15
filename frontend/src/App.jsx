import './App.css'
import MainContent from './components/MainContent'
import Header from './components/Header'
import backgroundImage from './assets/AdobeStock_722269965.jpeg'

function App() {
  return (
    <>
      <img class="background-img" src={backgroundImage}/>
      <Header/>
      <MainContent/>
    </>
  )
}

export default App
