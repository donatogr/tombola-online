export interface Game {
    id: number;
    status: string;
    current_number: number;
    extracted_numbers: number[];
}

export interface Card {
    id: number;
    user: number;
    game: number;
    numbers: number[][];
} 