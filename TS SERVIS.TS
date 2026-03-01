import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, map } from 'rxjs';
import { Character, CharactersApiResponse } from './character.model';

@Injectable({
  providedIn: 'root'
})
export class CharacterService {
  private readonly apiUrl = 'https://rickandmortyapi.com/api/character';

  constructor(private readonly http: HttpClient) {}

  getCharacters(): Observable<Character[]> {
    return this.http
      .get<CharactersApiResponse>(this.apiUrl)
      .pipe(map((response) => response.results));
  }
}
