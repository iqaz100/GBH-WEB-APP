import { Component, OnInit } from '@angular/core';

export interface SubSubCategory{
  id: string;
  name: string;
  description?: string;
}

export interface SubCategory{
  id: string;
  name: string;
  description?: string;
  subSubCategories: SubSubCategory[];
}

export interface Category{
  id: string;
  name: string;
  description?: string;
  subCategories: SubCategory[];
}

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.scss']
})
export class MenuComponent implements OnInit {

  categories: Category[] = [] as Category[];

  subCategoriesOne: SubCategory[] = [] as SubCategory[];
  subCategoriesTwo: SubCategory[] = [] as SubCategory[];
  subCategoriesThree: SubCategory[] = [] as SubCategory[];
  subCategoriesFour: SubCategory[] = [] as SubCategory[];

  subSubCategoriesOne: SubSubCategory[] = [] as SubSubCategory[];
  subSubCategoriesTwo: SubSubCategory[] = [] as SubSubCategory[];
  subSubCategoriesThree: SubSubCategory[] = [] as SubSubCategory[];
  subSubCategoriesFour: SubSubCategory[] = [] as SubSubCategory[];

  ngOnInit(): void {

    let subsubcategory1: SubSubCategory = {id: "a", name: "Buty sportowe", description: "xsxszzzz"}
    let subsubcategory2: SubSubCategory = {id: "b", name: "Buty wysokie", description: "hr"}
    let subsubcategory3: SubSubCategory = {id: "c", name: "Klapki", description: "123523"}
    let subsubcategory4: SubSubCategory = {id: "d", name: "Buty zimowe", description: "123523"}
    let subsubcategory5: SubSubCategory = {id: "e", name: "Bluzy", description: "xsxszzzz"}
    let subsubcategory6: SubSubCategory = {id: "f", name: "Kurtki", description: "hr"}
    let subsubcategory7: SubSubCategory = {id: "g", name: "Koszulki", description: "123523"}
    let subsubcategory8: SubSubCategory = {id: "h", name: "Spodnie", description: "123523"}
    let subsubcategory9: SubSubCategory = {id: "j", name: "Zegarki", description: "xsxszzzz"}
    let subsubcategory10: SubSubCategory = {id: "k", name: "Portfele", description: "hr"}
    let subsubcategory11: SubSubCategory = {id: "l", name: "Naszyjniki", description: "123523"}
    let subsubcategory12: SubSubCategory = {id: "m", name: "Bransoletki", description: "123523"}
    let subsubcategory13: SubSubCategory = {id: "n", name: "Piłki do koszykówki", description: "xsxszzzz"}
    let subsubcategory14: SubSubCategory = {id: "q", name: "Rakietki tenisowe", description: "hr"}
    let subsubcategory15: SubSubCategory = {id: "r", name: "Ochraniacze", description: "123523"}
    let subsubcategory16: SubSubCategory = {id: "i", name: "Stoły do ping ponga", description: "123523"}

    this.subSubCategoriesOne.push(subsubcategory1, subsubcategory2, subsubcategory3, subsubcategory4)
    this.subSubCategoriesTwo.push(subsubcategory5, subsubcategory6, subsubcategory7, subsubcategory8)
    this.subSubCategoriesThree.push(subsubcategory9, subsubcategory10, subsubcategory11, subsubcategory12)
    this.subSubCategoriesFour.push(subsubcategory13, subsubcategory14, subsubcategory15, subsubcategory16)


    let subcategory1: SubCategory = {id: "a", name: "Obuwie", description: "xsxszzzz", subSubCategories: this.subSubCategoriesOne}
    let subcategory2: SubCategory = {id: "b", name: "Odzież", description: "hr", subSubCategories: this.subSubCategoriesTwo}
    let subcategory3: SubCategory = {id: "c", name: "Akcesoria", description: "123523", subSubCategories: this.subSubCategoriesThree}
    let subcategory4: SubCategory = {id: "d", name: "Sport", description: "123523", subSubCategories: this.subSubCategoriesFour}

    this.subCategoriesOne.push(subcategory1, subcategory2, subcategory3, subcategory4)
    this.subCategoriesTwo.push(subcategory1, subcategory2, subcategory3, subcategory4)
    this.subCategoriesThree.push(subcategory1, subcategory2, subcategory3, subcategory4)
    this.subCategoriesFour.push(subcategory1, subcategory2, subcategory3, subcategory4)

    let category1: Category = {id: "1", name: "Mężczyzna", description: "xsxsxsxszzzzzzzzzzzz", subCategories: this.subCategoriesOne}
    let category2: Category = {id: "2", name: "Kobieta", description: "hgrgrgr", subCategories: this.subCategoriesTwo}
    let category3: Category = {id: "3", name: "Dziecko", description: "123523", subCategories: this.subCategoriesThree}
    let category4: Category = {id: "4", name: "Inne", description: "asada523", subCategories: this.subCategoriesFour}

    this.categories.push(category1, category2, category3, category4)

    throw new Error('Method not implemented.');

  }

}




