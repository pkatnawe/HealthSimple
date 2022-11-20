import { useLocation } from 'react-router-dom';
import MainTopbar from '../MainTopbar/MainTopbar';
import './SummaryPage.css';

const SummaryPage = () => {
    const location = useLocation();
    const ingredientInfo = location.state.ingredientInfo;
    const mealInfo = location.state.mealInfo;


    const mealHTML = () => {
        return (
            <div className="meal-row">
                        <div className="score-container">
                            <div className="score">{mealInfo.score}</div>
                        </div>
                        <div className="summary-container">
                            <div className="summary">
                                {mealInfo.info}
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
                                <i className="fa-solid fa-chevron-right"></i> Goddamn I'm such a good cs student holy fuck
                                </h2>
                                A compiler is a tool that takes code as input and produces error messages. As a side-effect, it may produce an executable.
                                A compiler is a tool that takes code as input and produces error messages. As a side-effect, it may produce an executable.
                                A compiler is a tool that takes code as input and produces error messages. As a side-effect, it may produce an executable.
                            </div>
                        </div>

                        <div className="article-summary-container">
                            <div className="article-summary">
                                <h2 className="article-title">
                                <i className="fa-solid fa-chevron-right"></i> Goddamn I'm such a good cs student holy fuck
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
