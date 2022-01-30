import React,{Component} from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
import UseClick from './UseClick';
import UseEffectPractice from './UseEffectPractice';
import UseTitle from './UseTitle';
import Useconfirm from './Useconfirm'
import UseprevnetLeave from './UseprevnetLeave'
import Practice from './Practice';
import Usebeforeleave from './Usebeforeleave';
import Usefadein from './Usefadein';
import Usenetwork from './Usenetwork';
import Usescroll from './Usescroll';
import Usefullscreen from './Usefullscreen';
import Usenotification from './Usenotification';
import Useaxiosc from './Useaxiosc';
export default function App() {
  return (
    <div className="App">
      <Practice/>
      <hr/>
      <UseEffectPractice/>
      <hr/>
      <UseTitle/>
      <hr/>
      <UseClick/>
      <hr/>
      <Useconfirm/>
      <hr/>
      <UseprevnetLeave/>
      <hr/>
      <Usebeforeleave/>
      <hr/>
      <Usefadein/>
      <hr/>
      <Usenetwork/>
      <hr/>
      <Usescroll/>
      <hr/>
      <Usefullscreen/>
      <hr/>
      <Usenotification/>
      <hr/>
      <Useaxiosc/>
    </div>
  );
}

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
