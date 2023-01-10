import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomePageComponent } from './pages/home-page/home-page.component';
import { MainComponent } from './core/main/main.component';
import { LoginPageComponent } from './pages/login-page/login-page.component';
import { LoginComponent } from './features/login-fields/login/login.component';
import { RegisterComponent } from './features/login-fields/register/register.component';
import { ReminderComponent } from './features/login-fields/reminder/reminder.component';
import {MatFormFieldModule} from '@angular/material/form-field';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatOptionModule } from '@angular/material/core';
import { MatSelectModule } from '@angular/material/select';
import { MatIconModule } from '@angular/material/icon'


@NgModule({
  declarations: [
    AppComponent,
    HomePageComponent,
    MainComponent,
    LoginPageComponent,
    LoginComponent,
    RegisterComponent,
    ReminderComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatFormFieldModule,
    BrowserAnimationsModule,
    MatOptionModule,
    MatSelectModule,
    MatIconModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
