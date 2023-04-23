import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/shared/services/api.service';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent implements OnInit {
  constructor(private api: ApiService){}

  /**
   * Przykład wykorzystania ApiService to odpytania serwera o listę produktów.
   * TODO: Do usunięcia w przyszłości
   */
  ngOnInit(): void {
    console.log("tu")
    this.api.products.list().subscribe({
      next: x => {
        console.log(x)
      }
    })
  }
}
