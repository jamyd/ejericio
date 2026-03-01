import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { Character } from './character.model';
import { CharacterService } from './character.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {
  characters: Character[] = [];
  loading = true;
  error = '';

  constructor(private readonly characterService: CharacterService) {}

  ngOnInit(): void {
    this.characterService.getCharacters().subscribe({
      next: (characters) => {
        this.characters = characters;
        this.loading = false;
      },
      error: () => {
        this.error = 'No fue posible cargar los personajes.';
        this.loading = false;
      }
    });
  }
}
