const ResultBox = ({ value, color }) => {
    let colorClass = 'default';
  
    if (color === 'green') {
        colorClass = 'green';
    } else if (color === 'yellow') {
        colorClass = 'yellow';
    }

    return (
        <div className={`result-box ${colorClass}`}>
            <p><strong>{value}</strong></p>
        </div>
    );
};

export default ResultBox;
