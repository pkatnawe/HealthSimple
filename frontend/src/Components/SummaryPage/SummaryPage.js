// import { useNavigate } from 'react-router-dom';
import MainTopbar from '../MainTopbar/MainTopbar';
import './SummaryPage.css';

const SummaryPage = () => {
    // const navigate = useNavigate();
    // const goBack = () => {
    //     navigate(-1);
    // }
    return (
        <>
            <MainTopbar></MainTopbar>
            {/* <button className="back-btn" onClick={goBack}><i class="fa-solid fa-chevron-left"></i><span class="back-txt">Back</span></button> */}
            <div className='summary-page-container'>
                <div className="sub-container">
                    <h1>Meal score</h1>
                    <div className="meal-row">
                        <div className="score-container">
                            <div className="score">88</div>
                        </div>
                        <div className="summary-container">
                            <div className="summary">this is why no one loves you this is why no one loves you this is why no one loves you this is why no one loves you </div>
                        </div>
                    </div>


                    
                    <h1 className="your-food-txt">Your meal, at a glance</h1>
                    <div className="food-grid-container">
                        <div className="food-row">
                            <div className="food-grid">
                                <div className="food-txt">kale</div>
                            </div>
                            <div className="food-grid">
                                <div className="food-txt">kale</div>
                            </div>
                        </div>

                        <div className="food-row">
                            <div className="food-grid">
                                <div className="food-txt">kale</div>
                            </div>
                            <div className="food-grid">
                                <div className="food-txt">kale</div>
                            </div>
                        </div>

                        <div className="food-row">
                            <div className="food-grid">
                                <div className="food-txt">kale</div>
                            </div>
                        </div>
                    </div>



                    <h1 className="your-food-txt">You might want to read...</h1>
                    <div className="article-summary-section">

                        <div className="article-summary-container">
                            <div className="article-summary">
                                <h2 className="article-title">
                                    Goddamn I'm such a good cs student holy fuck
                                </h2>
                                A compiler is a tool that takes code as input and produces error messages. As a side-effect, it may produce an executable.
                                A compiler is a tool that takes code as input and produces error messages. As a side-effect, it may produce an executable.
                                A compiler is a tool that takes code as input and produces error messages. As a side-effect, it may produce an executable.
                            </div>
                        </div>

                        <div className="article-summary-container">
                            <div className="article-summary">
                                <h2 className="article-title">
                                    Goddamn I'm such a good cs student holy fuck
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
