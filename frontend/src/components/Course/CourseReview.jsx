import "./CourseReview.css";

function CourseReview( {username, message, rating, timestamp} ) {
    return (   
        <div className="course-review">
            <div className="review-header">
                <div className="review-userData">
                    <p className="review-username">{username} -</p>
                    <div className="review-stars">
                        {[1, 2, 3, 4, 5].map((n) => (
                            <span
                                key={n}
                                className={n <= rating ? "review-star filled" : "review-star"}
                            >
                                ★
                            </span>
                        ))}
                    </div>
                </div>
                <p className="review-timestamp">{timestamp}</p>
            </div>
            <span className="review-message">{message}</span>

        </div>
    );
}

export default CourseReview;