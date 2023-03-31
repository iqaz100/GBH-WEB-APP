import { Component, Input } from '@angular/core';
import { SubCategory, SubSubCategory } from '../menu/menu.component';


@Component({
  selector: 'app-menu-subcategory',
  templateUrl: './menu-subcategory.component.html',
  styleUrls: ['./menu-subcategory.component.scss']
})
export class MenuSubcategoryComponent {
  @Input() subCategories: SubCategory[];
  @Input() subSubCategories: SubSubCategory[];
}

