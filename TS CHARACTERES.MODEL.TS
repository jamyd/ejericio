export interface Character {
  id: number;
  name: string;
  status: 'Alive' | 'Dead' | 'unknown';
  species: string;
  image: string;
}

export interface CharactersApiResponse {
  results: Character[];
}
