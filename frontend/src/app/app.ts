import { Component, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';


@Component({
	selector: 'app-root',
	imports: [CommonModule, FormsModule],
	template: `
<h1>Catálogo de Peças</h1>
    
    <div>
      <input 
        type="text" 
        [(ngModel)]="searchTerm" 
        placeholder="Pesquisar peças..."
      />
      <button (click)="search()">Pesquisar</button>
    </div>

    <div *ngIf="loading">
      <p>A pesquisar...</p>
    </div>

    <div *ngIf="results$ | async as results">
      <h2>Resultados:</h2>
      <pre>{{ results | json }}</pre>
    </div>  `,
	styles: [],
})

export class AppComponent {
	searchTerm: string = '';
	results$: Observable<any> | null = null;
	loading: boolean = false;

	constructor(private http: HttpClient) { }

	search() {
		this.loading = true;
		const url =
			`http://localhost:8000/api/search?q=${encodeURIComponent(this.searchTerm)}`

		this.results$ = this.http.get(url).pipe(
			tap(() => this.loading = false),
			catchError(error => {
				console.error("Search error: ", error);
				this.loading = false;
				return of(null);
			})
		);
	}
}
