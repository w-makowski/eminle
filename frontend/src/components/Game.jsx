import { useState, useEffect } from 'react'
import { startGame, checkGuess } from '../api'
import GuessInput from './GuessInput'
import GuessList from './GuessList'


const Game = () => {
    const [gameId, setGameId] = useState(null);
    const [guessesLeft, setGuessesLeft] = useState(10);
    const [hints, setHints] = useState([]);
    const [gameOver, setGameOver] = useState(false);
    const [message, setMessage] = useState("");

    useEffect(() => {
        async function fetchGame() {
            const data = await startGame();
            setGameId(data.game_id);
            setGuessesLeft(data.guesses_left);
            console.log("data", data);
        }
        fetchGame();
    }, []);

    const handleGuess = async (guess) => {
        if (!gameId || gameOver) return;
        setMessage("");

        console.log("Submitting guess:", guess);
        console.log("Game id:", gameId);
    
        try {
            const response = await checkGuess(gameId, guess);
            console.log("API Response:", response);
            
            if (response.message) {
                setMessage(response.message)
            } else {
                if (response.won) {
                    setGameOver(true);
                    setMessage('You won!');
                }
        
                setGuessesLeft(response.guesses_left);
                setHints([...hints, response.guess]);
            }
    
            if (response.guesses_left === 0) {
                setGameOver(true);
                setGuessesLeft(0);
                setMessage(`Game Over! The correct song was: ${response.correct_song.song_name}`);
            }
        } catch (error) {
            console.error("Error submitting guess:", error);
        }

    }

    return (
        <div className="game-container">
            <div className="fixed-section">
                <div className="game-status">
                    <p>Guesses Left: {guessesLeft}</p>
                </div>
                    <div className="game-message">
                        <p className={gameOver ? (message.includes('won') ? 'win-message' : 'lose-message') : ''}>{message}</p>
                    </div>
                {!gameOver && <GuessInput onGuess={handleGuess} />}
            </div>
            <div className="guesses-section">
                <GuessList hints={hints} />
            </div>
        </div>
    );

};

export default Game;
