import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainComponent } from './core/main/main.component';
import { HomePageComponent } from './pages/home-page/home-page.component';

const routes: Routes = [
  {path: '', component: MainComponent, children: [
    {path: '', redirectTo: 'home', pathMatch: 'full'},
    {path: 'home', component: HomePageComponent}
  ]}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
