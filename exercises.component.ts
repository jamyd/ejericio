import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

/**
 * Displays step-by-step solutions for the four differential equation
 * exercises of the university math workshop. Each exercise includes the
 * applied rule, the mathematical model, the procedure, and a final result
 * highlighted in a red box as required by the workshop guidelines.
 */
@Component({
  selector: 'app-exercises',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './exercises.component.html',
  styleUrl: './exercises.component.css'
})
export class ExercisesComponent {}
