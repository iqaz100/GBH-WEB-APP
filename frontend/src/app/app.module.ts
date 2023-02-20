import { NgModule} from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomePageComponent } from './pages/home-page/home-page.component';
import { MainComponent } from './core/main/main.component';
import { MenuComponent } from './features/nav-bar/menu-bar/menu/menu.component';
import { MenuSubcategoryComponent } from './features/nav-bar/menu-bar/menu-subcategory/menu-subcategory.component';
import { NavBarComponent } from './features/nav-bar/nav-bar/nav-bar.component';
import { NavButtonsComponent } from './features/nav-bar/nav-buttons/nav-buttons.component';

import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import { MatTabsModule } from '@angular/material/tabs';
import { LogoContainerComponent } from './features/nav-bar/logo-container/logo-container.component';



@NgModule({
  declarations: [
    AppComponent,
    HomePageComponent,
    MainComponent,
    MenuComponent,
    MenuSubcategoryComponent,
    NavBarComponent,
    NavButtonsComponent,
    LogoContainerComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatTabsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
