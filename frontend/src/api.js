const API_URL = "http://127.0.0.1:8000/api";

export const startGame = async () => {
    const response = await fetch(`${API_URL}/start-game/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
    });
    return response.json();
};

export const checkGuess = async (gameId, guess) => {
    const response = await fetch(`${API_URL}/check-guess/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ game_id: gameId, guess }),
    });
    return response.json();
};

export const getSongSuggestions = async (query) => {
    const response = await fetch(`${API_URL}/suggest-songs/?q=${encodeURIComponent(query)}`);
    return response.json();
};
