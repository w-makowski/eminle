import { useState, useEffect } from 'react';
import { getSongSuggestions } from '../api';


const GuessInput = ({ onGuess }) => {
    const [guess, setGuess] = useState('');
    const [suggestions, setSuggestions] = useState([]);
    const [showSuggestions, setShowSuggestions] = useState(false);

    useEffect(() => {
        const fetchSuggestions = async () => {
            if (guess.length < 2) {
                setSuggestions([]);
                return;
            }

            try {
                const results = await getSongSuggestions(guess);
                setSuggestions(results);
                setShowSuggestions(true);
            } catch (error) {
                console.error("Error fetching suggestions:", error);
            }
        };

        const debounce = setTimeout(fetchSuggestions, 300);
        return () => clearTimeout(debounce);
    }, [guess]);

    const handleSubmit = (e) => {
        e.preventDefault();
        if (guess.trim()) {
            onGuess(guess);
            setGuess("");
            setSuggestions([]);
            setShowSuggestions(false);
        }
    };

    const handleSuggestionClick = (name) => {
        setGuess('');
        setSuggestions([]);
        setShowSuggestions(false);
        onGuess(name);
    }

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={guess}
                onChange={(e) => setGuess(e.target.value)}
                placeholder="Enter a song name..."
                autoComplete="off"
            />
            <button type="submit">Guess</button>

            {showSuggestions && suggestions.length > 0 && (
                <ul>
                    {suggestions.map((s) => (
                      <li
                        key={s.id}
                        onClick={() => handleSuggestionClick(s.name)}
                      >
                        {s.name}
                      </li>
                    ))}
                </ul>
            )}
        </form>
    )
};

export default GuessInput;
