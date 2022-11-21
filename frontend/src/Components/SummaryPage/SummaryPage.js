import { useLocation } from 'react-router-dom';
import MainTopbar from '../MainTopbar/MainTopbar';
import './SummaryPage.css';
import axios from "axios";
import { useEffect, useState } from "react";

const SummaryPage = () => {
    const location = useLocation();
    const ingredientInfo = location.state.ingredientInfo;
    // const mealInfo = location.state.mealInfo;
    const url = location.state.url;
    let [mealGrade, setMealGrade] = useState('');
    let [color, setColor] = useState('')
    let [mealInfo, setMealInfo] = useState('')

    const helpMe = (data) => {
        setMealGrade(data)
        if (data === 'A') {
            setColor('green')
        } else if (data === 'B') {
            setColor('MediumTurquoise')
        } else if (data === 'C') {
            setColor('orange')
            
        } else if (data === 'D') {
            setColor('red')
        }
        console.log(color)
    }
    useEffect(() => {
        axios
          .get(`http://localhost:5000/api/score/${url}`, { mode: "cors" })
          .then((res) =>  helpMe(res.data))
          .then((res) => console.log(mealGrade))
          .catch((err) => console.log(err));
    }, []);

    useEffect(() => {
        axios
          .get(`http://localhost:5000/api/data/${url}`, { mode: "cors" })
          .then((res) => {setMealInfo(res.data.split('Answer:')[1].replace('--', ''));
        console.log(res)})
          .catch((err) => console.log(err));
    }, []);



    const mealHTML = () => {
        return (
            <div className="meal-row">
                        <div className="score-container" style={{backgroundColor: color}}>
                            <div className="score">{mealGrade}</div>
                        </div>
                        <div className="summary-container">
                            <div className="summary">
                                {mealInfo}
                            </div>
                        </div>
            </div>
        ); 
    }

    const foodsHTML = ingredientInfo.map((food, index) => {
        return (
            <div key={index} className="food-summary-container">
                <div className="food-summary">
                    <h2 className="food-title">
                    <i className="fa-solid fa-chevron-right"></i> {food.name}
                    </h2>
                    {food.info}
                </div>
            </div>
        );
    })

    // const loading = () => {
    //     if (pageLoading) {
    //         return (
    //             <h1 className='loading'>cmon co:here YOU GOT THISSS</h1>
    //         )
    //     }
    // }


    return (
        <>
            <MainTopbar></MainTopbar>
            <div className='summary-page-container'>
                <div className="sub-container">
                    <h1>Meal score</h1>
                    {mealHTML()}


                    
                    <h1 className="your-food-txt">Your food, at a glance</h1>
                    
                    <div className="food-summary-section">

                        {foodsHTML}
            
                    </div>




                    <h1 className="your-food-txt">You might want to read...</h1>
                    <div className="article-summary-section">

                        <div className="article-summary-container">
                            <div className="article-summary">
                                <h2 className="article-title">
                                <i className="fa-solid fa-chevron-right"></i> Research shows that staying up late for hackathons might not be sustainable
                                </h2>
                                A compiler is a tool that takes code as input and produces error messages. As a side-effect, it may produce an executable.
                                A compiler is a tool that takes code as input and produces error messages. As a side-effect, it may produce an executable.
                                A compiler is a tool that takes code as input and produces error messages. As a side-effect, it may produce an executable.
                            </div>
                        </div>

                        <div className="article-summary-container">
                            <div className="article-summary">
                                <h2 className="article-title">
                                <i className="fa-solid fa-chevron-right"></i> why uoft might be better than the university of ...
                                </h2>
                                A compiler is a tool that takes code as input and produces error messages. As a side-effect, it may produce an executable.
                                A compiler is a tool that takes code as input and produces error messages. As a side-effect, it may produce an executable.
                                A compiler is a tool that takes code as input and produces error messages. As a side-effect, it may produce an executable.
                            </div>
                        </div>
                        

                    </div>
                </div>

                
            </div>
        </>
    );
    

};

export default SummaryPage;
