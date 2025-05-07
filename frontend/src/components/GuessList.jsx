import ResultBox from "./ResultBox";

const GuessList = ({ hints }) => {
    return (
        <div className="guesses-list">
            <h3>Your Guesses:</h3>
            
            <div className="categories-header">
                <div className="categories-box"><p/> Song Name</div>
                <div className="categories-box"><p/> Album</div>
                <div className="categories-box"><p/> Track Number</div>
                <div className="categories-box"><p/> Track Length</div>
                <div className="categories-box"><p/> Features</div>
            </div>

            {/* Renderowanie bloków z danymi */}
            {hints.map((hint, index) => (
                <div
                    key={index}
                    className="guess-row"
                >
                    <ResultBox
                        value={hint.song_name}
                    />
                    <ResultBox
                        value={`${hint.album.value} (${hint.album.hint})`}
                        color={hint.album.color}
                    />
                    <ResultBox
                        value={`${hint.track_number.value} (${hint.track_number.hint})`}
                        color={hint.track_number.color}
                    />
                    <ResultBox
                        value={`${hint.track_length.value} (${hint.track_length.hint})`}
                        color={hint.track_length.color}
                    />
                    <ResultBox
                        value={hint.features.value}
                        color={hint.features.color}
                    />
                </div>
            ))}
        </div>
    );
};

export default GuessList;
