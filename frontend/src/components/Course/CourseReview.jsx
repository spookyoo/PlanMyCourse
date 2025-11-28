import "./CourseReview.css";

function CourseReview( {username, message, rating, timestamp} ) {
    return (   
        <div className="course-review">
            <div className="review-header">
                <div className="review-userData">
                    <p className="review-username">{username}</p>
                    <p></p>
                </div>
                <p className="review-timestamp">{timestamp}</p>
            </div>
            <span className="review-message">{message}</span>

        </div>
    );
}

export default CourseReview;