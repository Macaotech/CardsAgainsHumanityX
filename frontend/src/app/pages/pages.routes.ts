import { Routes } from '@angular/router';
import { GameComponent } from './game/game.component';
import { LobbyComponent } from './lobby/lobby.component';
import { HomeComponent } from './home/home.component';

export const PagesRoute: Routes = [
  {path: '', component: HomeComponent},
  {path: 'game/:id', component: GameComponent},
  {path: 'lobby', component: LobbyComponent},
];
